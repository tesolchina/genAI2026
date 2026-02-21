import os, json, base64, time, sys
from pathlib import Path
from dotenv import load_dotenv
import openai

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = openai.OpenAI(
    api_key=os.getenv("POE_API_KEY"),
    base_url="https://api.poe.com/v1",
)

KEYFRAMES_DIR = Path(__file__).resolve().parent / "keyframes"
OUTPUT_FILE = Path(__file__).resolve().parent / "keyframes" / "ocr_results.json"

PROMPT = """Analyze this screenshot from a Zoom workshop recording. The screen shows a shared screen view from a Cursor IDE session or browser. Identify:

1. **screen_content_type**: What is on screen? (e.g., "IDE with file open", "browser showing webpage", "slides/presentation", "terminal", "Zoom gallery view", "video playback", "file explorer")
2. **file_paths**: Any file paths visible in the IDE sidebar or editor tabs (list them exactly as shown)
3. **urls**: Any URLs visible in the browser address bar or on screen
4. **slide_title**: If showing slides/presentation, what is the title or heading
5. **visible_text_summary**: Brief summary of the main visible text content (2-3 sentences max)
6. **ide_active_file**: If IDE is open, what file is currently active/focused in the editor

Respond in valid JSON only. No markdown formatting, no code fences. Example:
{"screen_content_type": "IDE with file open", "file_paths": ["KissingNumber/Ref/SCMPreport.md"], "urls": [], "slide_title": null, "visible_text_summary": "The editor shows the SCMP report about kissing number research", "ide_active_file": "SCMPreport.md"}"""


def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def frame_to_timestamp(frame_num: int, interval: int = 20) -> str:
    total_seconds = (frame_num - 1) * interval
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def ocr_frame(frame_path: str, retries: int = 3) -> dict:
    b64 = encode_image(frame_path)
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="GPT-4o",
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": PROMPT},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
                    ],
                }],
                max_tokens=500,
                stream=False,
            )
            text = response.choices[0].message.content.strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
            return json.loads(text)
        except json.JSONDecodeError:
            print(f"  [warn] JSON parse failed for {frame_path}, attempt {attempt+1}, raw: {text[:200]}")
            if attempt < retries - 1:
                time.sleep(2)
        except Exception as e:
            print(f"  [error] API call failed for {frame_path}: {e}")
            if attempt < retries - 1:
                time.sleep(5)
    return {"error": "failed after retries", "raw": text if 'text' in dir() else ""}


def main():
    frames = sorted(KEYFRAMES_DIR.glob("frame_*.jpg"))
    print(f"Found {len(frames)} keyframes")

    existing = {}
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            existing = json.load(f)

    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else len(frames)

    results = existing.copy()
    processed = 0

    for frame_path in frames[start - 1:end]:
        frame_num = int(frame_path.stem.split("_")[1])
        timestamp = frame_to_timestamp(frame_num)
        key = frame_path.name

        if key in results and "error" not in results[key]:
            print(f"  [skip] {key} already processed")
            continue

        print(f"  [{frame_num}/{len(frames)}] {key} ({timestamp}) ...", end=" ", flush=True)
        result = ocr_frame(str(frame_path))
        result["timestamp"] = timestamp
        result["frame_number"] = frame_num
        results[key] = result
        processed += 1
        print("done")

        if processed % 10 == 0:
            with open(OUTPUT_FILE, "w") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"  [saved] {processed} frames processed so far")

        time.sleep(1)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nDone. {processed} new frames processed. Total: {len(results)}. Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
