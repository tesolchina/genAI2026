"""
Remove only significant silences (>= 5s) from the video.
Uses ffmpeg trim+concat with only ~45 segments (manageable filter graph).
Re-encodes with CRF 20 for high visual quality.
"""
import json, subprocess, sys
from pathlib import Path

DIR = Path(__file__).parent
INPUT = DIR / "workshop1_shared_screen_1920x1200.mp4"
OUTPUT = DIR / "workshop1_edited.mp4"
MIN_SILENCE = 5.0
MARGIN = 0.5


with open(DIR / "silence_data.json") as f:
    data = json.load(f)

silences = [(s["start"], s["end"]) for s in data["silences"]
            if s["end"] - s["start"] >= MIN_SILENCE]
total_dur = data["stats"]["original_duration"]

print(f"Original duration: {total_dur/60:.1f} min")
print(f"Significant silences (>= {MIN_SILENCE}s): {len(silences)}")
print(f"Total silence to remove: {sum(e-s for s,e in silences):.0f}s ({sum(e-s for s,e in silences)/60:.1f} min)")

segments = []
pos = 0.0
for s_start, s_end in silences:
    seg_end = s_start + MARGIN
    if seg_end > pos + 0.5:
        segments.append((pos, seg_end))
    pos = max(s_end - MARGIN, seg_end)
if pos < total_dur:
    segments.append((pos, total_dur))

edited_dur = sum(e - s for s, e in segments)
print(f"Segments to keep: {len(segments)}")
print(f"Expected edited duration: {edited_dur/60:.1f} min")
print(f"Expected reduction: {(total_dur - edited_dur)/60:.1f} min ({(1-edited_dur/total_dur)*100:.1f}%)")

n = len(segments)
vtrims = [f"[0:v]trim=start={s:.3f}:end={e:.3f},setpts=PTS-STARTPTS[v{i}]" for i, (s, e) in enumerate(segments)]
atrims = [f"[0:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS[a{i}]" for i, (s, e) in enumerate(segments)]
vinputs = "".join(f"[v{i}]" for i in range(n))
ainputs = "".join(f"[a{i}]" for i in range(n))
fc = ";".join(vtrims + atrims) + f";{vinputs}concat=n={n}:v=1:a=0[outv];{ainputs}concat=n={n}:v=0:a=1[outa]"

cmd = [
    "ffmpeg", "-y", "-i", str(INPUT),
    "-filter_complex", fc,
    "-map", "[outv]", "-map", "[outa]",
    "-c:v", "libx264", "-crf", "20", "-preset", "fast",
    "-c:a", "aac", "-b:a", "128k",
    str(OUTPUT)
]

print(f"\nRunning ffmpeg with {n} segments (CRF 20, preset fast)...")
print(f"This will take 15-30 minutes for a 105-min video...")
sys.stdout.flush()

result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print(f"ERROR (exit {result.returncode}):")
    print(result.stderr[-2000:])
    sys.exit(1)

probe = subprocess.run(
    ["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", str(OUTPUT)],
    capture_output=True, text=True
)
final_dur = float(json.loads(probe.stdout)["format"]["duration"])
size_mb = OUTPUT.stat().st_size / 1024 / 1024

probe2 = subprocess.run(
    ["ffprobe", "-v", "quiet", "-show_streams", "-print_format", "json", str(OUTPUT)],
    capture_output=True, text=True
)
streams = json.loads(probe2.stdout)
for s in streams.get("streams", []):
    if s["codec_type"] == "video":
        print(f"  Video: {s['width']}x{s['height']}, {s['codec_name']}, bitrate={s.get('bit_rate','?')}")

print(f"\nDone!")
print(f"  Original:  {total_dur/60:.1f} min ({data['stats']['original_duration']/1024/1024:.0f} MB)")
print(f"  Edited:    {final_dur/60:.1f} min")
print(f"  Removed:   {(total_dur-final_dur)/60:.1f} min ({(1-final_dur/total_dur)*100:.1f}%)")
print(f"  File size: {size_mb:.0f} MB")
print(f"  Output:    {OUTPUT}")
