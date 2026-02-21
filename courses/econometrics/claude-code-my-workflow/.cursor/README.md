# Cursor Replication of Sant'Anna Claude Code Workflow

This folder contains **Cursor-native** skills and rules that replicate the [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) behavior inside Cursor.

## What's included

### Skills (`.cursor/skills/`)

| Skill | What it does |
|-------|----------------|
| `proofread` | Grammar, typos, overflow, consistency — report only |
| `visual-audit` | Slide layout audit (overflow, fonts, box fatigue, spacing) |
| `pedagogy-review` | 13-pattern teaching review (narrative, notation, pacing) |
| `review-r` | R code quality, reproducibility, domain correctness |
| `qa-quarto` | Adversarial Quarto vs Beamer (critic → fixer loop, max 5 rounds) |
| `slide-excellence` | Combined visual + pedagogy + proofread (+ optional TikZ/parity) |
| `memory-and-learn` | Read MEMORY.md; append [LEARN] on user corrections |

**Usage:** In Cursor, ask in natural language, e.g. "Run proofread on Slides/Lecture01.tex", "Do a full slide-excellence review of Quarto/lecture1.qmd", "Review R scripts in scripts/R", "Read memory and apply learnings".

### Rules (`.cursor/rules/`)

| Rule | Scope | What it enforces |
|------|--------|-------------------|
| `plan-first-workflow` | Always | Plan non-trivial tasks, save to quality_reports/plans/, get approval |
| `quality-gates` | .tex, .qmd, .R | 80 commit, 90 PR, 95 excellence; block below 80 |
| `single-source-of-truth` | Figures, Slides, Quarto | Beamer is source; derive Quarto/figures from it |
| `session-logging` | Always | Log to quality_reports/session_logs/ after plan, during work, at end |
| `replication-protocol` | .R | Replicate original results before extending; tolerances |
| `exploration-folder` | explorations/ | Experiments in explorations/; 60 bar; graduate at 80 |
| `memory-learn` | Always | Read MEMORY.md at start; append [LEARN] on corrections |

## How this differs from Claude Code CLI

- **One agent:** Cursor has a single agent. "Multi-agent" review is done by the same agent following different skills in sequence (e.g. slide-excellence runs visual, pedagogy, proofread one after another).
- **No native hooks:** There is no automatic pre-compact or post-merge hook. You can run scripts in `.claude/hooks/` manually or ask the agent to run them (e.g. "run the pre-compact script").
- **MEMORY.md:** Implemented via the `memory-learn` rule and `memory-and-learn` skill; the agent reads and appends as specified.

## Quick start

1. Open **this project root** (the folder containing `.cursor/` and `CLAUDE.md`) in Cursor.
2. Optionally say: "Read MEMORY.md and apply any [LEARN] entries for this session."
3. For reviews: "Proofread Slides/Lecture01.tex", "Run slide-excellence on Quarto/lecture1.qmd", "Review all R scripts in scripts/R".
4. For QA: "Run qa-quarto for Lecture1" (critic then fixer in sequence until approved or 5 rounds).

Original workflow: [Sant'Anna blog](https://psantanna.com/claude-code-my-workflow/) · [GitHub](https://github.com/pedrohcgs/claude-code-my-workflow).
