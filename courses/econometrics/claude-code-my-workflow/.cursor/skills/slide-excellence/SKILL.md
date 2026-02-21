---
name: slide-excellence
description: Run combined multi-dimensional slide review: visual audit, pedagogy review, and proofreading (and optionally TikZ parity). Use when the user asks for full or comprehensive slide review before a milestone.
---

# Slide Excellence Review

Run a combined review: visual + pedagogy + proofreading (and TikZ/parity if relevant). Produce one synthesized report.

## Steps

1. **Identify the file** from the user's message (in `Quarto/` or `Slides/`).

2. **Run these reviews** (you are one agent doing all roles in sequence):
   - **Visual audit:** overflow, fonts, box fatigue, spacing → `quality_reports/[FILE]_visual_audit.md`
   - **Pedagogy:** 13 patterns, narrative, pacing, notation → `quality_reports/[FILE]_pedagogy_report.md`
   - **Proofread:** grammar, typos, consistency → `quality_reports/[FILE]_report.md`
   - **TikZ** (if file has TikZ): labels, geometry, semantics → `quality_reports/[FILE]_tikz_review.md`
   - **Content parity** (if .qmd with .tex): frame count, content drift → `quality_reports/[FILE]_parity_report.md`

3. **Synthesize** a single summary:

```markdown
# Slide Excellence: [Filename]
## Overall: EXCELLENT / GOOD / NEEDS WORK / POOR
| Dimension    | Critical | Medium | Low |
| Visual       | ...     | ...   | ... |
| Pedagogical  | ...     | ...   | ... |
| Proofreading | ...     | ...   | ... |
### Critical (fix first)
### Medium (next revision)
### Next steps
```

4. **Rubric:** Excellent 0–2 critical / 0–5 medium; Good 3–5 / 6–15; Needs Work 6–10 / 16–30; Poor 11+ / 31+.
