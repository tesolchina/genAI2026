"""
Segment the edited video into chapters based on content analysis.
Maps original timestamps to edited timestamps using silence_data.json.
Splits using ffmpeg stream copy (fast, no re-encoding).
"""
import json, subprocess, sys
from pathlib import Path

DIR = Path(__file__).parent
INPUT = DIR / "workshop1_edited.mp4"
MIN_SILENCE = 5.0
MARGIN = 0.5

with open(DIR / "silence_data.json") as f:
    sd = json.load(f)

silences = [(s["start"], s["end"]) for s in sd["silences"]
            if s["end"] - s["start"] >= MIN_SILENCE]

# Chapters defined by ORIGINAL timestamps (before silence removal)
chapters = [
    ("Part01_welcome",          "Welcome & Workshop Overview — What Is Agentic AI 101?",                          0,     600),
    ("Part02_agents_vs_chatbots", "AI Agents vs Chatbots — How IDE Agents Read, Write & Act on Your Files",       600,   1500),
    ("Part03_curriculum_reform", "Why We Must Revamp Education — The SCMP Letter & the Kissing Number Problem",   1500,  2100),
    ("Part04_research_with_ai",  "Finding a Research Paper with an AI Agent — Live arXiv Search Demo",            2100,  2730),
    ("Part05_brainstorm_draft",  "From Paper to Letter — AI-Powered Brainstorming & Drafting in the IDE",         2730,  3300),
    ("Part06_video_chinese",     "Multi-Tool Workflow — Video Analysis, Chinese Notes & Cross-Platform AI",       3300,  3900),
    ("Part07_visual_data",       "Telling a Visual Story — PackingStar Data, GitHub Repos & AI Narration",        3900,  4620),
    ("Part08_ambassador_panel",  "Student Ambassador Panel — Reflections on Learning with AI Agents",             4620,  5160),
    ("Part09_hands_on_demo",     "Hands-On Demo — A Student Clones a Repo & Writes a Letter with AI in VS Code", 5160,  5850),
    ("Part10_wrap_up",           "Wrap-Up — GitHub Pages, Exam Prep Ideas & Getting Started with Trae",           5850,  6320),
]


def orig_to_edited(orig_t):
    """Convert original timestamp to edited timestamp by subtracting removed silence."""
    removed = 0.0
    for s_start, s_end in silences:
        cut_start = s_start + MARGIN
        cut_end = s_end - MARGIN
        if cut_end <= cut_start:
            continue
        if orig_t <= cut_start:
            break
        elif orig_t >= cut_end:
            removed += (cut_end - cut_start)
        else:
            removed += (orig_t - cut_start)
            break
    return orig_t - removed


def fmt_time(seconds):
    h = int(seconds) // 3600
    m = (int(seconds) % 3600) // 60
    s = int(seconds) % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


print("Chapter Plan (original → edited timestamps):\n")
print(f"{'#':>2}  {'Filename':<30}  {'Original':>15}  {'Edited':>15}  {'Duration':>8}  Title")
print("-" * 110)

for i, (fname, title, orig_start, orig_end) in enumerate(chapters):
    ed_start = orig_to_edited(orig_start)
    ed_end = orig_to_edited(orig_end)
    dur = ed_end - ed_start
    print(f"{i+1:2d}  {fname:<30}  {fmt_time(orig_start)}-{fmt_time(orig_end)}  {fmt_time(ed_start)}-{fmt_time(ed_end)}  {dur/60:5.1f}m  {title}")

print()

seg_dir = DIR / "segments"
seg_dir.mkdir(exist_ok=True)

chapters_data = []

for i, (fname, title, orig_start, orig_end) in enumerate(chapters):
    ed_start = orig_to_edited(orig_start)
    ed_end = orig_to_edited(orig_end)
    dur = ed_end - ed_start
    outfile = seg_dir / f"{fname}.mp4"

    print(f"  Splitting {fname} ({dur/60:.1f} min)...", end=" ", flush=True)

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(ed_start),
        "-i", str(INPUT),
        "-t", str(dur),
        "-c", "copy",
        "-avoid_negative_ts", "1",
        str(outfile)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr[-300:]}")
    else:
        size = outfile.stat().st_size / 1024 / 1024
        print(f"done ({size:.0f} MB)")

    chapters_data.append({
        "index": i + 1,
        "filename": fname + ".mp4",
        "title": title,
        "original_start": fmt_time(orig_start),
        "original_end": fmt_time(orig_end),
        "edited_start": fmt_time(ed_start),
        "edited_end": fmt_time(ed_end),
        "duration_min": round(dur / 60, 1),
    })

with open(DIR / "chapters.json", "w") as f:
    json.dump(chapters_data, f, indent=2)
print(f"\nSaved chapters.json")

# Generate VTT chapters file
with open(DIR / "chapters.vtt", "w") as f:
    f.write("WEBVTT\n\n")
    for ch in chapters_data:
        f.write(f"{ch['edited_start']}.000 --> {ch['edited_end']}.000\n")
        f.write(f"{ch['title']}\n\n")
print("Saved chapters.vtt")

print(f"\nDone! {len(chapters)} segments in segments/ folder.")
