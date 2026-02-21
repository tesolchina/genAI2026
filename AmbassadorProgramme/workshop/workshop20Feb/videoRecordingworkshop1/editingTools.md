# Automatic Video Editing Tools for Zoom Workshop Recordings

A curated list of open-source and AI-powered tools for automatically editing Zoom meeting/workshop recordings.

---

## 1. auto-editor (Recommended for Quick Cleanup)

- **GitHub:** https://github.com/WyattBlue/auto-editor
- **Stars:** ~4,000
- **Language:** Nim / Python CLI
- **License:** Unlicense (public domain)

**Summary:** Command-line tool that automatically removes silence and dead space from video/audio. Acts as a "first pass" editor — feed it a Zoom recording and it cuts out all the quiet/dead moments. Supports audio-loudness-based and motion-based detection. Can export edit timelines to Adobe Premiere Pro, DaVinci Resolve, Final Cut Pro, ShotCut, and Kdenlive for further manual refinement.

**Key Features:**
- Silence detection and removal with configurable thresholds
- Motion-based editing (useful for screen-share heavy workshops)
- Adjustable margin/padding around cuts for smooth transitions
- Export to professional NLE timelines (Premiere XML, FCPXML, etc.)
- Clip sequence export to split video into individual segments

**Install:** `pip install auto-editor`

**Example:** `auto-editor workshop_recording.mp4 --margin 0.3s`

---

## 2. FunClip (Recommended for Content-Based Clipping)

- **GitHub:** https://github.com/modelscope/FunClip
- **Stars:** ~5,300
- **Language:** Python (Gradio UI)
- **License:** MIT

**Summary:** Fully open-source, locally-deployed AI video clipping tool from Alibaba's ModelScope. Uses industrial-grade Paraformer speech recognition to transcribe your video, then lets you select text segments or speakers to generate clips. Since v2.0, it integrates LLMs (Qwen, GPT) to intelligently identify and clip relevant segments using customizable prompts.

**Key Features:**
- High-accuracy ASR with timestamp prediction (Paraformer-Large, 13M+ downloads)
- Speaker recognition via CAM++ — clip by specific speaker
- LLM-based smart clipping with custom prompts (e.g., "extract Q&A sections")
- Multi-segment clipping with automatic SRT subtitle generation
- Hotword customization for domain-specific terms
- Supports Chinese and English audio
- Gradio web UI for easy interaction

**Use Case:** Ideal for extracting highlights, specific topics, or individual speaker segments from a workshop recording.

---

## 3. Cut.py (Best for AI-Selected Highlights)

- **GitHub:** https://github.com/arafat2020/cut_py
- **Language:** Python
- **License:** Open source

**Summary:** AI-powered video highlight generator using local LLM models (Llama 3 via llama.cpp). Transcribes video with Faster Whisper, detects scenes with PySceneDetect, and uses an LLM to select the most engaging or relevant segments. You can request specific types of highlights (e.g., "key takeaways" or "most interesting discussions").

**Key Features:**
- Faster Whisper transcription (fast and accurate)
- Scene detection via PySceneDetect
- LLM-based intelligent segment selection
- Docker-containerized FFmpeg for consistent processing
- Customizable highlight prompts

---

## 4. easyEdits (Prompt-Based Editing)

- **GitHub:** https://github.com/robinroy03/easyedits
- **Language:** Python
- **License:** Open source

**Summary:** Prompt-based video editing tool. Uses OpenAI Whisper for transcription, scenedetect for automatic clip splitting, and Gemini for audio descriptions. Offers a version-control-style editing workflow. Self-hostable.

**Key Features:**
- Natural language editing commands
- Whisper-based transcription
- Automatic scene detection and splitting
- Version-control-style workflow

---

## 5. ClipsAI Video Editor (Long-Form to Clips)

- **GitHub:** https://github.com/clipsai/video-editor
- **Stars:** Growing community
- **Language:** TypeScript (UI) + Python (ClipsAI library)
- **License:** MIT

**Summary:** Designed to convert long-form video (podcasts, interviews, workshops) into short clips. The Python library analyzes transcripts to identify self-contained segments, then the TypeScript UI lets you trim and resize. Good for creating shareable workshop highlights.

**Key Features:**
- Transcript-based segment identification
- Simple trim and resize UI
- Optimized for long-form-to-short-form conversion

---

## 6. Transcript Seeker (Transcript-Synchronized Viewer)

- **GitHub:** https://github.com/Meeting-BaaS/transcript-seeker
- **Language:** TypeScript
- **License:** Open source

**Summary:** Browser-based transcript viewer with synchronized video playback. Upload recordings, transcribe via Gladia or AssemblyAI, and chat with transcripts using OpenAI. Integrates with Meeting Baas bots for Zoom, Google Meet, and Teams. More of a review/navigation tool than an editor, but useful for identifying what to cut.

**Key Features:**
- Live transcript seeking synced with video
- AI chat with transcript content
- Multi-platform meeting bot integration

---

## 7. Twick (React Video Editor SDK)

- **GitHub:** https://github.com/ncounterspecialist/twick
- **Stars:** ~370
- **Language:** TypeScript / React
- **License:** Open source

**Summary:** AI-powered video editor SDK built with React. Features a canvas timeline, drag-and-drop editing, AI captions, and serverless MP4 export. More of a building block for custom video editing apps than a ready-to-use tool.

---

## Recommendations

### For a Zoom Workshop Recording, Here Is the Suggested Workflow:

| Step | Tool | Purpose |
|------|------|---------|
| **Step 1** | **auto-editor** | Remove all silence/dead space as a first pass. This alone can cut a 2-hour recording down significantly. |
| **Step 2** | **FunClip** | Transcribe the cleaned video, then use LLM prompts or speaker selection to extract specific segments (e.g., "main presentation", "Q&A", "demo sections"). |
| **Step 3** | Export to DaVinci Resolve / Premiere (optional) | Use auto-editor's timeline export for any manual fine-tuning. |

### Quick Comparison

| Tool | Best For | Difficulty | Local/Cloud | AI-Powered |
|------|----------|------------|-------------|------------|
| auto-editor | Silence removal, first-pass cleanup | Easy (CLI) | Local | No (rule-based) |
| FunClip | Speaker/topic-based clipping | Easy (Web UI) | Local | Yes (ASR + LLM) |
| Cut.py | AI highlight extraction | Medium | Local | Yes (local LLM) |
| easyEdits | Prompt-based editing | Medium | Local | Yes (Whisper + Gemini) |
| ClipsAI | Long-form to short clips | Medium | Local | Yes (transcript) |
| Transcript Seeker | Review and navigate recordings | Easy (Web) | Cloud APIs | Yes (ASR + chat) |

### Top Pick

**Start with `auto-editor`** — it requires zero configuration, installs with a single pip command, and instantly removes dead air from your workshop recording. Then use **FunClip** if you need to extract specific segments by speaker or topic. This two-tool combination covers most workshop video editing needs without requiring any cloud services or API keys.
