---
name: qa-quarto
description: Adversarial QA comparing Quarto slides to Beamer benchmark. Run critic (find issues) then fixer (apply fixes); repeat until approved or max 5 rounds. Use when the user asks to QA Quarto vs Beamer or validate a lecture translation.
---

# Adversarial Quarto vs Beamer QA

Beamer PDF is the gold standard. Quarto must match or exceed it.

## Hard gates (non-negotiable)

- No content cut off (overflow)
- Interactive charts ≥ static where applicable
- Content parity (no missing slides/equations/text)
- Visual quality ≥ Beamer
- Slide centering stable; notation verbatim from Beamer

## Workflow (single agent, two phases per round)

1. **Critic phase:** Compare Beamer (.tex/.pdf) and Quarto (.qmd/.html) for the lecture. List every issue (Critical / Major / Minor). Save to `quality_reports/[Lecture]_qa_critic_roundN.md`. If no blocking issues, state "APPROVED" and stop.

2. **Fixer phase:** Apply fixes from the critic report (Critical first, then Major, then Minor). Re-render Quarto. Do not self-approve.

3. **Re-audit:** Run critic again on the updated Quarto. If not APPROVED and rounds < 5, repeat from step 2. After 5 rounds, report remaining issues to the user.

4. **Final report:** Save `quality_reports/[Lecture]_qa_final.md` with gate status and any remaining issues.

## Pre-flight

- Locate Beamer and Quarto files; re-render if .qmd newer than .html; verify TikZ SVGs if used.
