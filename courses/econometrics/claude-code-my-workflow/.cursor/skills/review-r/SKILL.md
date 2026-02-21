---
name: review-r
description: Review R scripts for code quality, reproducibility, and domain correctness. Checks set.seed, paths, structure, figure quality, and conventions. Use when the user asks to review R code or check scripts in scripts/R or Figures.
---

# Review R Scripts

Run the R code review protocol. **Produce reports only** — do not edit R files.

## Steps

1. **Identify scripts** from the user's message (one file, "LectureN", or "all"). Look in `scripts/R/`, `Figures/*/`, and project `.R` files.

2. **For each script, check** (use `.claude/rules/r-code-conventions.md` if present):
   - **Structure & header:** title, author, purpose, sections
   - **Reproducibility:** single `set.seed()` at top, relative paths, no absolute paths, `dir.create()` for outputs
   - **Console hygiene:** no `cat()`/`print()` for status; use `message()` sparingly
   - **Functions:** snake_case, documentation, no magic numbers
   - **Domain correctness:** estimator matches theory, correct standard errors, correct estimand (e.g. ATT vs ATE)
   - **Figure quality:** transparent bg for Beamer, explicit dimensions, readable fonts

3. **Save report** to `quality_reports/[script_name]_r_review.md`. Use severity: Critical / High / Medium / Low.

4. **Do NOT edit R source files.** Present summary: issues per script, severity breakdown, top critical issues.
