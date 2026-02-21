---
name: proofread
description: Run proofreading on lecture files (.tex or .qmd). Checks grammar, typos, overflow, consistency, and academic quality. Produces a report only; does not edit files. Use when the user asks to proofread slides or check grammar/typos in lecture content.
---

# Proofread Lecture Files

Run the proofreading protocol on lecture files. Produce a **report only** — do not edit source files.

## Steps

1. **Identify files** from the user's message (e.g. a path like `Slides/Lecture01.tex` or `Quarto/lecture1.qmd`). If "all", review all in `Slides/` and `Quarto/`.

2. **For each file, check:**
   - **Grammar:** subject-verb agreement, articles, prepositions, tense
   - **Typos:** misspellings, duplicated words, artifacts
   - **Overflow:** overfull hbox (LaTeX), content exceeding slide bounds (Quarto)
   - **Consistency:** citation format, notation, terminology
   - **Academic quality:** informal language, missing words, awkward phrasing

3. **Produce a report** per file with: location, current text, proposed fix, category, severity. Save to `quality_reports/[FILENAME]_report.md` (for .qmd use `_qmd_report.md`).

4. **Do NOT edit any source files.** Only produce the report. Present a summary (total issues, breakdown, critical items).

## Report format (per issue)

```markdown
### Issue N: [Brief description]
- **File:** [filename]
- **Location:** [slide or line]
- **Current:** "[exact text]"
- **Proposed:** "[fix]"
- **Category:** Grammar / Typo / Overflow / Consistency / Academic Quality
- **Severity:** High / Medium / Low
```
