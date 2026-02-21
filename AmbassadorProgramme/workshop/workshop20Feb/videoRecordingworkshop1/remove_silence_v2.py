"""
Remove silence from video using ffmpeg trim+concat filter.
Uses silence_data.json from previous detection run.
Re-encodes with CRF 20 for high visual quality.
"""
import json, subprocess, sys
from pathlib import Path

DIR = Path(__file__).parent
INPUT = DIR / "workshop1_shared_screen_1920x1200.mp4"
OUTPUT = DIR / "workshop1_edited.mp4"
SILENCE_DATA = DIR / "silence_data.json"

with open(SILENCE_DATA) as f:
    data = json.load(f)

segments = data["segments"]
n = len(segments)
print(f"Segments to keep: {n}")
print(f"Expected duration: {data['stats']['edited_duration']/60:.1f} min")

# Build trim+concat filter graph
video_trims = []
audio_trims = []
for i, seg in enumerate(segments):
    s, e = seg["start"], seg["end"]
    video_trims.append(
        f"[0:v]trim=start={s:.3f}:end={e:.3f},setpts=PTS-STARTPTS[v{i}]"
    )
    audio_trims.append(
        f"[0:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS[a{i}]"
    )

video_inputs = "".join(f"[v{i}]" for i in range(n))
audio_inputs = "".join(f"[a{i}]" for i in range(n))

filter_complex = ";".join(video_trims + audio_trims) + \
    f";{video_inputs}concat=n={n}:v=1:a=0[outv]" + \
    f";{audio_inputs}concat=n={n}:v=0:a=1[outa]"

cmd = [
    "ffmpeg", "-y", "-i", str(INPUT),
    "-filter_complex", filter_complex,
    "-map", "[outv]", "-map", "[outa]",
    "-c:v", "libx264", "-crf", "20", "-preset", "fast",
    "-c:a", "aac", "-b:a", "128k",
    str(OUTPUT)
]

print(f"\nRunning ffmpeg with {n} trim segments...")
print(f"This will take several minutes (re-encoding at CRF 20)...")

result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    err = result.stderr
    print(f"ERROR (exit {result.returncode}):")
    print(err[-2000:])
    sys.exit(1)

dur_cmd = ["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", str(OUTPUT)]
dur_result = subprocess.run(dur_cmd, capture_output=True, text=True)
final_dur = float(json.loads(dur_result.stdout)["format"]["duration"])
size_mb = OUTPUT.stat().st_size / 1024 / 1024

print(f"\nDone!")
print(f"  Original:  {data['stats']['original_duration']/60:.1f} min")
print(f"  Edited:    {final_dur/60:.1f} min")
print(f"  Removed:   {(data['stats']['original_duration']-final_dur)/60:.1f} min")
print(f"  File size: {size_mb:.0f} MB")
print(f"  Output:    {OUTPUT}")
