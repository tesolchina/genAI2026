# 5MarWorkshop — AI Agent Meets Textual Mentors

This project supports the **HKBU UCLC 1008 University English I** workshop (4 Mar 2026), with a focus on preparing first-year undergraduates for **Argumentation Construction and Evaluation (ACE)** tasks.

The workspace is designed as an **agentic learning workflow**: humans provide prompts in `Tasks/`, the AI agent reads context and source materials, and generated artifacts are stored in `Output/`.

---

## Workshop Purpose

- Help students prepare for in-class ACE writing and evaluation tasks.
- Organize source materials, assignment constraints, and writing models.
- Demonstrate how AI can support preparation (before assessment) through structured prompting, synthesis, and visualization.

---

## Project Structure

### `Context/`
Context-setting information about audience, teaching goals, and workshop framing.

- `overview.md`: workshop scenario, student profile, and title context.

### `Data/`
Core learning and reference materials.

- `ACE/`
	- `draftInstructions.md`: assignment constraints and timing.
	- `rubrics.md`: grading dimensions and expectations.
	- `practiceWritingTask.md`: mock ACE practice task.
	- `ACE sample 1.md`, `ACE sample 2.md`: sample writing references.
- `Literature/`
	- `HoReview.md`: key literature review used as topical source base.
- `module 3/`
	- `argumentModels.md`, `alternativeModels.md`: argument structure guidance.
	- `respondCounterargument.md`, `strategiesCounterargument.md`: rebuttal/counterargument techniques.
	- `AIprompts.md`: prompt patterns for AI-supported preparation.

### `Docs/`
User-facing documentation and instructional notes.

- `lesson1.md`: lesson-level documentation content.

### `Tasks/`
Prompt files that define what the AI agent should produce.

- `takeStock.md`: inventory and resource-index generation instructions.
- `identifyPapers.md`: paper identification and prioritization task.
- `PaperReviewed.md`: paper review instruction scaffold.
- `explainFramework.md`: instruction to generate dynamic workflow visualization.
- `fetch_abstracts.py`: helper script for literature-related workflow.

### `Output/`
Generated artifacts from tasks.

- `resourcesIndex.md`: structured prep resource guide.
- `resourcesIndex.html`: visual index for quick navigation.
- `relevantPapers.md`: prioritized literature shortlist.
- `paperReviewed.md`: synthesized review output.
- `framework.html`: dynamic animation of agentic file-processing workflow.

---

## How This Workflow Operates

1. Human defines a task in `Tasks/`.
2. Agent reads project intent (`Context/` + `readme.md`).
3. Agent gathers evidence from `Data/`.
4. Agent references instructional conventions in `Docs/`.
5. Agent generates deliverables into `Output/`.
6. Users review/refine outputs and iterate with new prompts.

---

## Suggested Use for Students

- Start with `Data/ACE/draftInstructions.md` and `Data/ACE/rubrics.md`.
- Study model and strategy files under `Data/module 3/`.
- Use `Data/Literature/HoReview.md` to anticipate likely source directions.
- Practice with `Data/ACE/practiceWritingTask.md`.
- Review generated syntheses in `Output/` for revision and planning.

---

## Suggested Use for Instructors

- Update task prompts in `Tasks/` for different cohorts.
- Add/replace source readings under `Data/`.
- Keep lesson notes in `Docs/`.
- Archive each run’s generated artifacts under `Output/`.

---

## Published Interactive Framework (GitHub Pages)

https://tesolchina.github.io/genAI2026/AmbassadorProgramme/workshop/5MarWorkshop/Output/framework.html
