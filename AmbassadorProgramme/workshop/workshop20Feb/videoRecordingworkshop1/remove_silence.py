"""
Detect silent segments using ffmpeg silencedetect, then concatenate
non-silent segments using stream copy (no re-encoding = original quality).
"""
import subprocess, re, json, sys
from pathlib import Path

INPUT = Path(__file__).parent / "workshop1_shared_screen_1920x1200.mp4"
OUTPUT = Path(__file__).parent / "workshop1_edited.mp4"
CONCAT_LIST = Path(__file__).parent / "concat_segments.txt"

SILENCE_THRESH = "-30dB"
SILENCE_DURATION = "2.0"
MARGIN = 0.3


def detect_silence(input_path):
    cmd = [
        "ffmpeg", "-i", str(input_path),
        "-af", f"silencedetect=noise={SILENCE_THRESH}:d={SILENCE_DURATION}",
        "-f", "null", "-"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    stderr = result.stderr

    silences = []
    starts = re.findall(r"silence_start: ([\d.]+)", stderr)
    ends = re.findall(r"silence_end: ([\d.]+)", stderr)

    for s, e in zip(starts, ends):
        silences.append((float(s), float(e)))

    return silences


def get_duration(input_path):
    cmd = ["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", str(input_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(json.loads(result.stdout)["format"]["duration"])


def compute_segments(silences, total_duration):
    segments = []
    pos = 0.0

    for silence_start, silence_end in silences:
        seg_end = silence_start + MARGIN
        seg_start = max(pos, 0.0)
        if seg_end <= seg_start:
            continue
        segments.append((seg_start, seg_end))
        pos = max(silence_end - MARGIN, seg_end)

    if pos < total_duration:
        segments.append((pos, total_duration))

    return segments


def build_select_expr(silences, total_duration):
    """Build ffmpeg select/aselect filter expression to keep non-silent parts."""
    parts = []
    pos = 0.0
    for s_start, s_end in silences:
        keep_end = s_start + MARGIN
        keep_start = max(s_end - MARGIN, keep_end)
        if keep_end > pos:
            parts.append(f"between(t,{pos:.3f},{keep_end:.3f})")
        pos = keep_start
    if pos < total_duration:
        parts.append(f"between(t,{pos:.3f},{total_duration:.3f})")
    return "+".join(parts)


def encode_without_silence(input_path, silences, total_duration, output_path):
    expr = build_select_expr(silences, total_duration)
    cmd = [
        "ffmpeg", "-y", "-i", str(input_path),
        "-vf", f"select='{expr}',setpts=N/FRAME_RATE/TB",
        "-af", f"aselect='{expr}',asetpts=N/SR/TB",
        "-c:v", "libx264", "-crf", "20", "-preset", "fast",
        "-c:a", "aac", "-b:a", "128k",
        str(output_path)
    ]
    print(f"  Running ffmpeg (CRF 20, preset fast)...")
    print(f"  Select filter has {len(silences)} silence gaps to remove")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ffmpeg error: {result.stderr[-500:]}")
        sys.exit(1)
    print(f"  Encoded to {output_path}")


def main():
    print(f"Input: {INPUT}")
    print(f"Silence threshold: {SILENCE_THRESH}, min duration: {SILENCE_DURATION}s, margin: {MARGIN}s")

    print("\nStep 1: Detecting silence...")
    silences = detect_silence(INPUT)
    print(f"  Found {len(silences)} silent segments")
    total_silence = sum(e - s for s, e in silences)
    print(f"  Total silence: {total_silence:.1f}s ({total_silence/60:.1f} min)")

    duration = get_duration(INPUT)
    print(f"  Video duration: {duration:.1f}s ({duration/60:.1f} min)")

    print("\nStep 2: Computing non-silent segments...")
    segments = compute_segments(silences, duration)
    total_kept = sum(e - s for s, e in segments)
    print(f"  {len(segments)} segments to keep, total: {total_kept:.1f}s ({total_kept/60:.1f} min)")
    print(f"  Reduction: {(1 - total_kept/duration)*100:.1f}%")

    with open(Path(__file__).parent / "silence_data.json", "w") as f:
        json.dump({
            "silences": [{"start": s, "end": e} for s, e in silences],
            "segments": [{"start": s, "end": e} for s, e in segments],
            "stats": {
                "original_duration": duration,
                "edited_duration": total_kept,
                "silence_removed": duration - total_kept,
                "reduction_pct": (1 - total_kept/duration) * 100,
            }
        }, f, indent=2)
    print("  Saved silence_data.json")

    print(f"\nStep 3: Encoding without silent segments (CRF 20, high quality)...")
    encode_without_silence(INPUT, silences, duration, OUTPUT)

    final_dur = get_duration(OUTPUT)
    print(f"\nDone!")
    print(f"  Original: {duration/60:.1f} min")
    print(f"  Edited:   {final_dur/60:.1f} min")
    print(f"  Removed:  {(duration-final_dur)/60:.1f} min ({(1-final_dur/duration)*100:.1f}%)")
    print(f"  Output:   {OUTPUT}")
    print(f"  Size:     {OUTPUT.stat().st_size / 1024 / 1024:.0f} MB")


if __name__ == "__main__":
    main()
