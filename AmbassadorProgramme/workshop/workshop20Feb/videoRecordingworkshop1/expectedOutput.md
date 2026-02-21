# Expected Output — Workshop 1 Video & Learning Package

## Final Deliverables

### 1. Edited Full Video (with PiP speaker overlay)
- **File:** `workshop1_final.mp4`
- **Description:** The shared screen recording with silence removed, and the active speaker view composited as a small picture-in-picture overlay in a corner. This gives viewers both the screen content and the presenter's face.
- **Duration:** ~83 min (down from 105 min after silence removal)
- **Upload to:** YouTube, Bilibili
- **Embed on:** simon.hkbu.me/aiworkshop

### 2. Chapter-Segmented Videos (10 segments)
Individual video clips for each major section, suitable for standalone viewing or playlist:

| # | Filename | Title | ~Duration |
|---|----------|-------|-----------|
| 1 | `segment_01_setup.mp4` | Workshop Setup & Introductions | 4 min |
| 2 | `segment_02_html_slides.mp4` | Why HTML Slides Instead of PowerPoint | 4 min |
| 3 | `segment_03_ai_agent_ide.mp4` | What Is an AI Agent & IDE | 8 min |
| 4 | `segment_04_kissing_number.mp4` | The Kissing Number Story | 8 min |
| 5 | `segment_05_ai_workflow.mp4` | AI Agent Workflow Demo | 17 min |
| 6 | `segment_06_visual_story.mp4` | Creating Visual Explanations with AI | 12 min |
| 7 | `segment_07_letter_drafting.mp4` | Writing with AI — Drafting a Letter | 8 min |
| 8 | `segment_08_student_discussion.mp4` | Student Ambassadors Discussion | 8 min |
| 9 | `segment_09_regina_demo.mp4` | Regina's Demo — AI for Writing Analysis | 10 min |
| 10 | `segment_10_closing.mp4` | Closing & Vision | 4 min |

Upload as: YouTube/Bilibili playlist

### 3. Timestamp-to-File Mapping (`keyframes/content_map.json`)
A structured JSON mapping each 20-second interval of the video to:
- What is on screen (IDE, browser, slides, terminal, etc.)
- Which files from `KissingNumber/` are being shown
- URLs visible on screen
- Summary of visible content

### 4. OCR Results (`keyframes/ocr_results.json`)
Raw OCR output from all 316 keyframes — the data source for the content map.

### 5. Video Chapters File (`chapters.json` and `chapters.vtt`)
- **chapters.json:** Machine-readable chapter data with timestamps, titles, descriptions, and linked files
- **chapters.vtt:** WebVTT chapters file for YouTube/player chapter markers

### 6. Learning Package Index (`index.html` or `learning_package.md`)
A landing page / table of contents for the full learning package:
- Embedded or linked video for each segment
- For each segment:
  - Brief summary of what is covered
  - Key takeaways
  - Links to the relevant files in `KissingNumber/` that are shown/discussed
  - Timestamps in the full video
- Full cleaned transcript with speaker labels
- Chat log with context
- Setup instructions for replication (for public audience with no prior knowledge)

### 7. Cleaned Transcript (`workshop1_transcript_clean.md`)
The Zoom auto-transcript cleaned up with:
- Proper speaker labels
- Paragraph grouping (not line-by-line)
- Timestamps at section boundaries
- Corrected obvious transcription errors

---

## Steps to Produce These Outputs

### Step 1: Silence Removal (DONE)
- **Tool:** auto-editor
- **Input:** `workshop1_shared_screen_1920x1200.mp4` (105 min, 548 MB)
- **Output:** `workshop1_edited.mp4` (83 min, 88 MB)
- **Status:** Complete

### Step 2: Keyframe Extraction (DONE)
- **Tool:** ffmpeg (1 frame every 20s)
- **Input:** `workshop1_shared_screen_1920x1200.mp4`
- **Output:** `keyframes/frame_0001.jpg` ... `frame_0316.jpg` (316 frames)
- **Status:** Complete

### Step 3: OCR on Keyframes (IN PROGRESS)
- **Tool:** Poe API (GPT-4o vision model)
- **Input:** 316 keyframe images
- **Output:** `keyframes/ocr_results.json`
- **Status:** Running (~35/316 done, ~25 min remaining)

### Step 4: Build Content Map
- **Tool:** Python script
- **Input:** `keyframes/ocr_results.json` + `workshop1_transcript.vtt`
- **Output:** `keyframes/content_map.json`
- **What it does:**
  - Merges OCR data with transcript timestamps
  - Groups consecutive frames with the same screen content into segments
  - Maps each segment to files in `KissingNumber/` by matching file paths from OCR against the actual folder structure
  - Identifies chapter boundaries where the screen content type or topic changes significantly

### Step 5: Create Chapter Markers
- **Tool:** Python script
- **Input:** `keyframes/content_map.json` + transcript analysis
- **Output:** `chapters.json`, `chapters.vtt`
- **What it does:**
  - Defines 10 chapter boundaries with titles and descriptions
  - Maps each chapter to the corresponding segment in the content map
  - Creates VTT chapter file for YouTube upload

### Step 6: Create PiP Composite Video
- **Tool:** ffmpeg
- **Input:** `workshop1_edited.mp4` (shared screen) + `workshop1_active_speaker_1920x1200.mp4` (speaker)
- **Output:** `workshop1_final.mp4`
- **What it does:**
  - Overlays the active speaker view as a small window (e.g., 320x200) in the bottom-right corner of the shared screen video
  - Both videos need to be time-aligned (they share the same start time from Zoom)
  - The PiP overlay needs to account for the silence cuts from auto-editor (the speaker video must be cut at the same points)
  - **Challenge:** auto-editor's cut timeline must be applied to the speaker video as well, or we composite first and then run auto-editor on the composite

### Step 7: Split into Segments
- **Tool:** ffmpeg
- **Input:** `workshop1_final.mp4` + `chapters.json`
- **Output:** `segment_01_setup.mp4` ... `segment_10_closing.mp4`
- **What it does:**
  - Splits the final composite video at chapter boundaries
  - Uses `-c copy` for fast splitting without re-encoding (where possible)

### Step 8: Clean Transcript
- **Tool:** Python script + LLM (Poe API)
- **Input:** `workshop1_transcript.vtt`
- **Output:** `workshop1_transcript_clean.md`
- **What it does:**
  - Groups rapid-fire subtitle lines into natural paragraphs
  - Adds section headings matching the chapters
  - Corrects obvious ASR errors (e.g., "chapel" → "chatbot", "kerpu" → "科普")
  - Preserves speaker labels

### Step 9: Assemble Learning Package
- **Tool:** Manual + LLM assistance
- **Input:** All outputs from Steps 1-8
- **Output:** `learning_package.md` or `index.html`
- **What it does:**
  - Creates a structured landing page
  - Links each segment video to its summary, transcript excerpt, and related files
  - Adds setup/replication instructions for new users
  - Designed for embedding on simon.hkbu.me/aiworkshop

### Step 10: Upload & Embed
- **Tool:** YouTube/Bilibili upload + website update
- **Input:** `workshop1_final.mp4`, segment videos, `chapters.vtt`
- **Output:** Published videos with chapter markers
- **What it does:**
  - Upload full video and segment playlist to YouTube and Bilibili
  - Add chapter markers from `chapters.vtt`
  - Embed on simon.hkbu.me/aiworkshop

---

## Current Progress

| Step | Status | Notes |
|------|--------|-------|
| 1. Silence removal | DONE | 105 min → 83 min |
| 2. Keyframes | DONE | 316 frames extracted |
| 3. OCR | IN PROGRESS | ~35/316 frames, ~25 min remaining |
| 4. Content map | WAITING | Depends on Step 3 |
| 5. Chapters | WAITING | Depends on Step 4 |
| 6. PiP composite | WAITING | Needs approach decision (see note below) |
| 7. Segments | WAITING | Depends on Steps 5-6 |
| 8. Clean transcript | READY | Can start independently |
| 9. Learning package | WAITING | Depends on Steps 5-8 |
| 10. Upload | WAITING | Depends on Step 9 |

### Note on Step 6 (PiP Composite)
Two possible approaches:
- **Option A:** Apply auto-editor's cut timeline to the speaker video first, then composite. More precise but requires extracting the cut list from auto-editor.
- **Option B:** Composite the raw shared screen + speaker video first (ffmpeg PiP overlay), then run auto-editor on the composite. Simpler but requires re-running auto-editor (~6 min processing).

Option B is recommended for simplicity.
