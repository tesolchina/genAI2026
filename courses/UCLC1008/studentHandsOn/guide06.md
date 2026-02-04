# Guide 06: Fix APA in-text citations in a paragraph

The AWQ requires **APA 7 in-text citations only** (no reference list, don’t cite the abstract). It’s easy to forget the “&” in parentheses or to put the citation in the wrong place. Use an AI agent to take **one paragraph** of your draft (or a sample paragraph with missing/wrong citations) and return a corrected version with brief notes—so you see exactly what “right” looks like.

**Input:**
1. One paragraph that either (a) has **no citations** but uses ideas from two authors, or (b) has **incorrect** APA (e.g. wrong order, “and” instead of “&” in parentheses, or citation only at the end of a long block).  
   Put it in a file, e.g. `genAI2026/courses/UCLC1008/studentHandsOn/paragraph_citationsToFix.md`.
2. Tell the AI which two sources you’re using (e.g. “Hong et al., 2022 and Andrejevic & Selwyn, 2020” for Sample AWQ, or “Skjuve et al., 2021 and Laestadius et al., 2022” for Practice 1). You can point to:  
   `genAI2026/courses/UCLC1008/AIagentDemo/taskOrientation.md`  
   item 3 for the three citation styles (author-prominent, signal-phrase, information-prominent).

**Process:** Ask the AI agent to:
1. Read your paragraph and the APA guidance in taskOrientation (item 3).
2. Insert or correct **APA 7 in-text citations** so each claim from Author A and Author B is clearly attributed.
3. Use a **mix** of styles where it reads naturally (e.g. author-prominent for the first mention, information-prominent for supporting points).
4. Add a **short note** under the paragraph: what was wrong or missing, and what rule was applied (e.g. “Use & in parentheses, not ‘and’”).

**Output:** Create a file in the same folder, e.g. `paragraph_citationsFixed.md`, containing:
- Your original paragraph
- Corrected paragraph with APA in-text citations
- “What was fixed” notes (3–5 bullets)

**Difficulties and challenges:**

...
...
...

**Tip:** In the exam you’ll do this under time pressure. Practising once with AI makes the rules stick—e.g. “(Author A & Author B, year)” in parentheses, “Author A and Author B (year)” in running text, and never citing the abstract. See also the examples in `genAI2026/courses/UCLC1008/AIagentDemo/taskOrientation.md` and in the Academic Writing Quiz Instructions.

Send the path of this file and your paragraph file to the AI agent to start.
