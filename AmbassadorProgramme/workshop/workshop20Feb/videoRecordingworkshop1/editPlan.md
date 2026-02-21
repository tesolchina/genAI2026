# Edit Plan — Workshop 1 Video & Learning Package

## Overview

**Workshop:** AI Agent Workshop #1 (20 Feb 2026)
**Duration:** 105 min (1h 45m)
**Presenter:** Simon Wang (with student ambassadors Regina/tszwai, Cici Luo, Lucia)
**Topic:** Using AI Agent (Cursor IDE) for science communication — Kissing Number / PackingStar case study
**Source material:** 4 video views, audio, Zoom transcript (927 entries), chat log, + full KissingNumber project folder

---

## Part A: Workshop Content Map

Based on transcript analysis, the workshop has these major sections:

| # | Time | Duration | Section | Key Content |
|---|------|----------|---------|-------------|
| 1 | 00:00–05:00 | 5 min | **Setup & Introductions** | Audio check, student ID rename, chat test |
| 2 | 05:00–10:00 | 5 min | **Workshop Page & HTML Slides** | simon.hkbu.me/aiworkshop, HTML vs PowerPoint, Replit vibe coding, edit mode demo |
| 3 | 10:00–15:00 | 5 min | **IDE Concept** | What is an IDE, VS Code / Cursor / Tray, folder + editor + AI panel layout |
| 4 | 15:00–25:00 | 10 min | **AI Agent Explained** | Chatbot vs Agent, why IDE matters, tool-use paradigm, hands-on setup page |
| 5 | 25:00–35:00 | 10 min | **Kissing Number Introduction** | SCMP article, PKU WeChat video playback, PackingStar research, science communication motivation |
| 6 | 35:00–55:00 | 20 min | **AI Agent Workflow Demo** | Finding the ArXiv paper, processing PKU video (keyframes + OCR + transcript alignment), Chinese notes analysis via Coze |
| 7 | 55:00–75:00 | 20 min | **Content Creation with AI** | Visual story (explain04.html), PackingStar data/viz, drafting SCMP letter, iterative prompting |
| 8 | 75:00–82:00 | 7 min | **Discussion: Student Ambassadors** | Regina (CS), Cici (Biology), Lucia (Business) — reflections on AI tools for their fields |
| 9 | 82:00–86:00 | 4 min | **Student Registration** | CCL credits, student IDs in chat |
| 10 | 86:00–100:00 | 14 min | **Regina's Demo** | Regina demonstrates her own AI agent work — letter analysis, writing style extraction |
| 11 | 100:00–105:00 | 5 min | **Closing** | Tray sponsorship/tokens, GitHub vision, future workshops, community building |

---

## Part B: File-to-Video Mapping (OCR Task)

Files/URLs shown on screen during the workshop (to be confirmed via OCR):

| Time (approx.) | File/URL Shown on Screen | KissingNumber Path |
|---|---|---|
| ~05:00 | simon.hkbu.me/aiworkshop/ | (external URL) |
| ~10:00 | simon.hkbu.me/aiworkshop/20feb | (external URL) |
| ~14:00 | Cursor IDE interface demo | (live demo) |
| ~25:00 | SCMP article on Kissing Number | `Ref/SCMPreport.md` |
| ~27:00 | PKU WeChat video playback | `Ref/PKU_wechat.mp4` |
| ~32:00 | searchPaper.md | `work/searchPaper.md` |
| ~35:00 | ArXiv paper 2511.13391 | `paper/2511.13391.html` |
| ~40:00 | Brainstorm.md | `work/Brainstorm.md` |
| ~45:00 | Keyframes from PKU video | `Ref/keyframes/` |
| ~48:00 | Chinese notes / Coze analysis | `Ref/ChineseNotesCoze.md` |
| ~50:00 | Aligned data (transcript + frames) | `Ref/aligned_data.json` |
| ~55:00 | Visual story slides (explain04.html) | `work/explain04.html` |
| ~60:00 | PackingStar data / visualizations | `PackingStar/viz/` |
| ~65:00 | Draft letter | `draftingLetter/draft01.md` → `draft03.md` |
| ~70:00 | Solar weather letter reference | `Ref/solarWeatherLetter.md` |
| ~90:00 | Regina's letter analysis work | (Regina's screen share) |
| ~100:00 | Tray token page / survey | simon.hkbu.me/aiworkshop/20feb/survey |

**Action needed:** Extract keyframes from `workshop1_shared_screen_1920x1200.mp4` at ~30s intervals, run OCR on each to identify exact file names and content shown. This will create a precise timestamp-to-file mapping.

---

## Part C: Proposed Editing Tasks

### Phase 1: Basic Cleanup (auto-editor)
1. Run `auto-editor` on the full shared screen video to remove silence/dead space
2. Estimated output: ~85-90 min (from 105 min, ~15-17% reduction)
3. Command: `~/auto-editor-bin workshop1_shared_screen_1920x1200.mp4 --margin 0.3s -o workshop1_edited.mp4`

### Phase 2: Keyframe Extraction & OCR
1. Extract keyframes from the shared screen video at 20-30s intervals using ffmpeg
2. Run OCR on each keyframe (tesseract or similar) to identify:
   - File names/paths visible in the Cursor IDE file explorer
   - URLs in the browser
   - Slide titles and content
3. Create a `keyframes/` subfolder with images and an `ocr_results.json`
4. Build a timestamp → file mapping table (refining Part B above)

### Phase 3: Chapter Segmentation
1. Use transcript + OCR data to create precise chapter boundaries
2. Generate a chapter file (VTT or JSON) for video player navigation
3. Chapters follow the 11-section structure from Part A

### Phase 4: Create Segment Videos
Split the edited video into standalone segments:

| Segment | Title | Approx. Duration | Priority |
|---------|-------|-------------------|----------|
| S1 | Introduction & Setup | 5 min | Low (skip for public) |
| S2 | Why HTML Slides Instead of PowerPoint | 5 min | Medium |
| S3 | What Is an AI Agent & IDE | 10 min | High |
| S4 | Kissing Number — The Story | 10 min | High |
| S5 | AI Agent Workflow Demo (Paper + Video Processing) | 20 min | High |
| S6 | Creating Visual Explanations with AI | 15 min | High |
| S7 | Writing with AI — Letter Drafting | 10 min | Medium |
| S8 | Student Ambassadors Discussion | 10 min | Medium |
| S9 | Regina's Demo — AI for Writing Analysis | 12 min | Medium |
| S10 | Closing & Vision | 5 min | Low |

### Phase 5: Learning Package Assembly
1. Create an `index.html` or `README.md` as a landing page for the learning package
2. For each segment, provide:
   - Video clip (or timestamp link to full video)
   - Summary of what's covered
   - Links to related files in KissingNumber/
   - Key takeaways
3. Include the full transcript (cleaned up, with speaker labels and timestamps)
4. Include the chat log with context

---

## Part D: Technical Approach for OCR-Based Linking

```
Workshop Video (shared screen)
        │
        ▼
   ffmpeg: extract keyframes (every 20-30s)
        │
        ▼
   ~200-300 keyframe images
        │
        ▼
   OCR (tesseract / Vision API)
        │
        ├── File paths visible in IDE sidebar
        ├── URLs in browser address bar
        ├── Content on slides
        └── Terminal commands
        │
        ▼
   Match with KissingNumber/ file tree
        │
        ▼
   Timestamp-to-File mapping (JSON)
        │
        ▼
   Chapter markers + cross-references
```

Tools needed:
- `ffmpeg` — keyframe extraction (already available)
- `tesseract` or Python `pytesseract` — OCR on keyframes
- Alternatively: use an LLM vision model (GPT-4V, Gemini) for more accurate screen content understanding
- `auto-editor` — silence removal (already installed)

---

## Part E: Priority & Suggested Order of Execution

| Priority | Task | Effort | Dependency |
|----------|------|--------|------------|
| 1 | Run auto-editor on full shared screen video | Low (1 command, ~20 min) | None |
| 2 | Extract keyframes from shared screen video | Low (ffmpeg, ~5 min) | None |
| 3 | Run OCR on keyframes | Medium (script needed) | Step 2 |
| 4 | Build timestamp-to-file mapping | Medium (analysis) | Step 3 |
| 5 | Create chapter markers | Low (manual + data from 3-4) | Steps 3-4 |
| 6 | Split into segment videos | Low (ffmpeg) | Steps 1, 5 |
| 7 | Create learning package index | Medium (writing) | Steps 4-6 |
| 8 | Clean up transcript | Low-Medium | None |

**Recommended starting point:** Run Steps 1 and 2 in parallel (both are quick), then proceed with Step 3 (OCR) which is the key enabling step for everything else.

---

## Decisions (Answered)

1. **Primary video view:** Shared screen (1920x1200) as main content, with active speaker overlaid as picture-in-picture (speaker on the side). Focus on shared screen view only — no separate edits of gallery or active-speaker-only views.

2. **Target audience:** Public audience with little knowledge about the setup. The learning package should provide enough information for viewers to replicate what was done in the workshop.

3. **Hosting platform:** Upload to YouTube and Bilibili. Embed in our own online platform at simon.hkbu.me/aiworkshop.

4. **OCR approach:** Use Poe API (OpenAI-compatible, vision model) for OCR on keyframes. API key stored in `workshop20Feb/.env` (gitignored). Base URL: `https://api.poe.com/v1`.

5. **Video views:** Focus solely on shared screen view with active speaker overlay (PiP composite).
