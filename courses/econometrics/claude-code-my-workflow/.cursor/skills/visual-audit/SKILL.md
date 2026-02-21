---
name: visual-audit
description: Perform visual layout audit of Quarto or Beamer slides. Checks overflow, font consistency, box fatigue, spacing, and layout. Use when the user asks for a visual or layout audit of slides.
---

# Visual Audit of Slide Deck

Perform a visual layout audit. Do not edit files; produce a report.

## Steps

1. **Identify the file** from the user's message (path in `Quarto/` or `Slides/`). If needed, render .qmd with `quarto render` or compile .tex to check overfull warnings.

2. **Audit every slide for:**
   - **Overflow:** content exceeding slide boundaries
   - **Font consistency:** inline font-size overrides, inconsistent sizes
   - **Box fatigue:** 2+ colored boxes on one slide, wrong box types
   - **Spacing:** missing negative margins, fig-align
   - **Layout:** missing transitions, framing, semantic colors

3. **Spacing-first principle** (for recommendations): (1) reduce vertical spacing / negative margins, (2) consolidate lists, (3) inline equations where possible, (4) reduce image size, (5) last resort: font size (never below 0.85em).

4. **Save report** to `quality_reports/[FILENAME]_visual_audit.md` and present a short summary.
