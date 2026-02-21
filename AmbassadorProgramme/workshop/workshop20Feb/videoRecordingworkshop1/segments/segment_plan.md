# Video Segmentation Plan

Based on full transcript analysis and alignment with the workshop slide page at
[simon.hkbu.me/aiworkshop/20feb](https://simon.hkbu.me/aiworkshop/20feb).

---

## Segments & Embedding Map

Each entry below specifies:
- **Where to embed**: the exact slide section heading on the page
- **Summary**: what the viewer will see and hear
- **Transcript range**: original timestamps from the raw recording

---

### Segment 1 — Welcome & Workshop Overview
- **Original time**: 0:00:16 – 0:09:57 (~9.7 min)
- **Embed after slide heading**: `Workshop Overview > Today's Plan`
- **Summary**: Simon opens the Zoom session, shares the workshop URL (simon.hkbu.me/aiworkshop), and demonstrates the HTML slide page — editing it live, showing how AI-generated HTML replaces PowerPoint. He explains why conventional GUI-based software (PowerPoint, Canva) will be disrupted by AI that builds custom interfaces on demand. He discusses the risk to knowledge workers and junior employees, references his SCMP letter on taxing AI, and officially welcomes participants with a Happy Chinese New Year. He walks through the registration page and workshop series plan.

---

### Segment 2 — What Are AI Agents? Agents vs Chatbots & the IDE
- **Original time**: 0:09:57 – 0:17:32 (~7.6 min)
- **Embed after slide heading**: `Key Concepts > AI Agent vs Chatbot & What Is an IDE?`
- **Also covers**: `Key Mindset`, `Breaking the Mental Barrier`
- **Summary**: Simon navigates to the hands-on instructions page and introduces the core concept: AI agents vs chatbots. He explains tool-calling — agents can read files, edit files, run code, and perform multi-step tasks. He shows the IDE layout (file explorer on the left, editor in the centre, AI chat on the right) and explains why this matters for non-programmers. He argues that IDEs are no longer just for software developers — they can be used by teachers, lawyers, doctors, and any knowledge worker to process documents. He mentions VS Code, Cursor, and Trae as IDE options.

---

### Segment 3 — Why This Matters: The 年兽 Monster & Curriculum Reform
- **Original time**: 0:17:32 – 0:25:18 (~7.8 min)
- **Embed after slide heading**: `Urgency > The 年兽 Monster`
- **Also covers**: revisits `Today's Plan` (demo/questionnaire/hands-on structure)
- **Summary**: Simon presents today's plan (30-min demo, exit questionnaire, hands-on session) and revisits the Agent vs Chatbot distinction. He discusses why teaching AI is hard — it's open-ended, you can only teach strategies and principles, not a finite set of skills. He introduces the 年兽 (Nian Shou) metaphor: AI is our monster, both exciting and threatening. He shows his published SCMP letter on AI and taxation, reads the line about universities needing concrete curriculum reform, and expresses frustration that education hasn't caught up. He commits to demonstrating what he means by "orchestrating AI processes."

---

### Segment 4 — The Kissing Number Story: SCMP Article & PKU Video
- **Original time**: 0:25:18 – 0:31:07 (~5.8 min)
- **Embed after slide heading**: `Case Study Introduction > The Kissing Number Project`
- **Summary**: Simon transitions to the case study. He introduces the SCMP article about PackingStar (Peking University, Fudan, Shanghai Academy of AI for Science) and the kissing number problem. He tries to play the PKU WeChat video, mentions contacting the journalist Victoria Bella. He explains his motivation: as a language teacher interested in science communication (科普), he wants to join the conversation by writing a letter to the SCMP editor. He shows the SCMP report saved in his project folder and the paper folder structure.

---

### Segment 5 — Finding the Paper: searchPaper.md & the arXiv API
- **Original time**: 0:31:07 – 0:38:19 (~7.2 min)
- **Embed after slide heading**: `The Prompt (searchPaper.md)`
- **Also covers**: `Transferable Technique: Agent as researcher`
- **Summary**: Simon states the goal: use an AI agent to find and download the research paper. He shows the `searchPaper.md` prompt file — "given the report, search arXiv to locate the paper." He demonstrates the agent reading the SCMP report, querying arXiv, and downloading the HTML paper into the `/paper` folder. He explains arXiv as an open-access database with an API (unlike paywalled Elsevier). He introduces the concept of API and explains why it matters. He shows that the entire project is synced to GitHub so participants can clone and replicate the work.

---

### Segment 6 — Multi-Task Prompting: Brainstorm.md & Two New Files
- **Original time**: 0:38:19 – 0:45:31 (~7.2 min)
- **Embed after slide heading**: `Key Advantage > Local Files as Context — Agent vs Chatbot`
- **Also covers**: `The Prompt (Brainstorm.md)`, `Output 1 · Process`, `Output 2 · Ideas`
- **Summary**: Simon explains the key advantage of an agent over a chatbot — all files in the project folder serve as context. He walks through the `Brainstorm.md` prompt, which references three local files (SCMP report, the paper, a previous solar weather letter) and a Poe chat history, and asks for two new files: `partnerAIwriting.md` (process analysis) and `ideas4letters.md` (brainstormed angles). He shows the agent creating both files, explains metacognition ("analyzing how you worked with AI before"), and shows the generated ideas including insights from the preprint not covered in the SCMP report.

---

### Segment 7 — Transferable Lessons: Metacognition & the Role of the Human
- **Original time**: 0:45:31 – 0:52:52 (~7.3 min)
- **Embed after slide heading**: `Think About Your Own Work`
- **Also covers**: extends discussion from `Output 1` and `Output 2`
- **Summary**: Simon discusses the risk and reward of using AI agents — students could ask AI to do everything, but the real question is "what role do you play?" He pushes back against colleagues who want to return to paper-based, in-class assessment, arguing that the workplace has already changed. He draws an analogy to how AI learns from training data (GitHub for code, Google Books for text) and how giving AI your own past work as training input is the same principle. He emphasizes that the key human skill is identifying strategies from past work and applying them to new contexts.

---

### Segment 8 — Processing a Chinese Video: OCR, YouTube Search & 3MT
- **Original time**: 0:52:52 – 1:00:17 (~7.4 min)
- **Embed after slide heading**: `Steps 9–10 · Video Processing`
- **Summary**: Simon explains how he processed the PKU WeChat video — screen-recording it (Tencent's closed ecosystem doesn't allow downloads), then using AI agent-written Python scripts to extract keyframes, run OCR, and align the transcript. He shows the machine-readable version of the video content. He then does a live demo: typing a prompt to search YouTube for 5 videos about AI agents and creating a `videoAgent.md` file. He mentions using the same approach for 3-Minute Thesis (3MT) video analysis. He contrasts Google's open API ecosystem with Tencent's closed one.

---

### Segment 9 — Building Explanation Decks: Iterative HTML Slides & PackingStar Data
- **Original time**: 1:00:17 – 1:08:06 (~7.8 min)
- **Embed after slide heading**: `Steps 11–13 · Explanation`
- **Also covers**: `Step 16 · Code Analysis`, `Step 17 · Visualization & Final Narrative`
- **Summary**: Simon wraps up the live demo and transitions to the explanation decks. He shows how he asked the agent to create HTML explainers — three iterative versions, each driven by specific feedback. He advocates that nobody should use PowerPoint anymore when AI can generate HTML slides with edit mode. He then shows explain04.html — the final 23-slide visual narrative with PKU video screenshots, PackingStar GitHub data visualizations, the final letter draft, and a transparency slide showing all 19 human/AI steps. He shows the agent cloning the PackingStar GitHub repo and generating visualizations from NumPy data.

---

### Segment 10 — Drafting the Letter: From Ideas to "AI Maths Romance"
- **Original time**: 1:08:06 – 1:12:53 (~4.8 min)
- **Embed after slide heading**: `Steps 14–19 · Drafting`
- **Summary**: Simon shows the letter drafting process — multiple drafts refined through human critical judgment. He navigates through the chat history and process log. He shows the final draft titled "AI maths romance is a two-way street," mentions he submitted it to SCMP yesterday, and shows the meta-slide about "how AI helped me write this." He delivers the core message: this demo should convince participants to try it themselves, and invites them to join a community to create new things together.

---

### Segment 11 — Exit Questionnaire & Open Floor
- **Original time**: 1:12:53 – 1:17:06 (~4.2 min)
- **Embed after slide heading**: `Action Required > Exit Questionnaire`
- **Summary**: Simon transitions from the demo to the exit questionnaire. He asks students needing CCL credits to leave their student ID in the Zoom chat. He shares the questionnaire link and gives participants a few minutes to complete it. He opens the floor for questions and invites student ambassadors Regina, Lucia, and CeCe to turn on cameras for a discussion.

---

### Segment 12 — Student Ambassador Panel: Regina, CeCe & Lucia
- **Original time**: 1:17:06 – 1:27:13 (~10.1 min)
- **Embed after slide heading**: `What We Covered Today` (or as standalone section)
- **Summary**: Three Year-2 student ambassadors share their perspectives. **Regina** (Computer Science) reflects on how AI agents change programming — "we don't really have to type the code now." **CeCe** (Biology) describes using agents to grab articles from websites and generate summaries for her own writing. **Lucia** (Business) shares a use case: asking an AI agent to sort and organize her messy desktop folder. Simon guides each student through the input → process → output framework and discusses the privacy considerations of letting agents access your files. He then invites audience participants to try a hands-on demo.

---

### Segment 13 — Hands-On Demo: Cloning a Repo & Analyzing a Letter in VS Code
- **Original time**: 1:27:13 – 1:41:15 (~14.0 min)
- **Embed after slide heading**: `Getting Started > Install Your IDE & Set Up Accounts`
- **Summary**: Regina shares her screen and opens VS Code. Simon guides her step by step: clone the workshop GitHub repo, navigate to the KissingNumber project files, find the solar weather letter. They compose a live prompt together: "analyze the styles, organization, and storytelling skills of this letter and generate lessons.html with actionable insights for future SCMP contributors." The agent produces a visually appealing HTML analysis page. Simon explains how to give more instructions (audience adaptation, color theme, GitHub Pages publishing, push as pull request). Regina mentions using AI for exam prep — uploading past papers and generating practice questions. They preview the generated `lessons.html`.

---

### Segment 14 — Closing: Trae Tokens, GitHub for All & Next Workshop
- **Original time**: 1:41:15 – 1:45:03 (~3.8 min)
- **Embed after slide heading**: `Bonus > Claim Your Trae Pro Code`
- **Also covers**: `Coming Up > Next Workshop`
- **Summary**: Simon acknowledges the Trae sponsorship and shows participants how to claim free Trae Pro tokens at the bottom of the workshop page. He shares his vision: every student and staff member at HKBU should have a GitHub account — "that would transform the entire institution." He frames AI agents as the future of language teaching: "we're not just teaching people to talk to other people, we're teaching people to talk to machines." He closes with thanks, announces the next workshop in early March, and invites everyone to bookmark the page and join the community.

---

## Embedding Summary Table

| Seg | Embed After This Slide Heading | Duration | Video Title |
|-----|-------------------------------|----------|-------------|
| 1 | `Workshop Overview > Today's Plan` | 9.7 min | Welcome & Workshop Overview |
| 2 | `Key Concepts > AI Agent vs Chatbot & What Is an IDE?` | 7.6 min | What Are AI Agents? Agents vs Chatbots & the IDE |
| 3 | `Urgency > The 年兽 Monster` | 7.8 min | Why This Matters: The 年兽 Monster & Curriculum Reform |
| 4 | `Case Study Introduction > The Kissing Number Project` | 5.8 min | The Kissing Number Story: SCMP Article & PKU Video |
| 5 | `The Prompt (searchPaper.md)` | 7.2 min | Finding the Paper: searchPaper.md & the arXiv API |
| 6 | `Key Advantage > Local Files as Context` | 7.2 min | Multi-Task Prompting: Brainstorm.md & Two New Files |
| 7 | `Think About Your Own Work` | 7.3 min | Transferable Lessons: Metacognition & the Role of the Human |
| 8 | `Steps 9–10 · Video Processing` | 7.4 min | Processing a Chinese Video: OCR, YouTube Search & 3MT |
| 9 | `Steps 11–13 · Explanation` | 7.8 min | Building Explanation Decks: Iterative HTML Slides & PackingStar |
| 10 | `Steps 14–19 · Drafting` | 4.8 min | Drafting the Letter: From Ideas to "AI Maths Romance" |
| 11 | `Action Required > Exit Questionnaire` | 4.2 min | Exit Questionnaire & Open Floor |
| 12 | `What We Covered Today` | 10.1 min | Student Ambassador Panel: Regina, CeCe & Lucia |
| 13 | `Getting Started > Install Your IDE` | 14.0 min | Hands-On Demo: Cloning a Repo & Analyzing a Letter |
| 14 | `Bonus > Claim Your Trae Pro Code` | 3.8 min | Closing: Trae Tokens, GitHub for All & Next Workshop |

---

## Transition Evidence (from transcript)

Key quotes that mark natural segment boundaries:

| Boundary | Timestamp | Speaker quote |
|---|---|---|
| 1→2 | 0:09:57 | "Anyone needs help to come to this page? ...type 2 if you can access this page" |
| 2→3 | 0:17:32 | "Okay, so… This is our slide. So today, we're going to talk about..." |
| 3→4 | 0:25:18 | "Alright... Now, this is relevant because I actually want to share with you how I wrote this letter" |
| 4→5 | 0:31:07 | "our goal is to use the AI agent in IDE to understand this research and write a letter" |
| 5→6 | 0:38:19 | "So that's kind of the first thing we do... now we have the paper, so we got a little bit more information" |
| 6→7 | 0:45:31 | "Are you with me? Are we good? So the AI agent was able to create two files" |
| 7→8 | 0:52:52 | "Now, the next part is also very exciting. Because what I did is I sent this whole video to AI" |
| 8→9 | 1:00:17 | "Sorry for the digression... I hope it's good enough to impress you" |
| 9→10 | 1:08:06 | "Then I start, drafting the letter. I'm gonna wrap up" |
| 10→11 | 1:12:53 | "here we go. So that's the demo... Great. So, there's this exit..." |
| 11→12 | 1:17:06 | "So, Lucia, Lucia and CC..." (stops sharing screen, starts panel) |
| 12→13 | 1:27:13 | "Do you guys want to do some hands-on... anyone who wants to share the screen" |
| 13→14 | 1:41:15 | "Thank you, Regina. There's one more thing I'd like to share..." |

---

## Status

- [ ] Review and confirm segment boundaries
- [ ] Edit transcript to remove unwanted parts (optional)
- [ ] Re-run segment_video.py with updated chapter definitions
- [ ] Verify each segment starts/ends cleanly
- [ ] Update chapters.json and chapters.vtt
- [ ] Embed videos into slide page
