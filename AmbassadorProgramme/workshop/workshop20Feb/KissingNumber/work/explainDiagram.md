# Explaining the PackingStar results diagram (`results_all.png`)

## What the diagram shows

The image contains **three panels**, all from the paper (arXiv:2511.13391, Figure 1). Together they summarise every new kissing number record PackingStar achieved.

---

## Key terms first

### What is "n-dimensional"?

- **Dimension** means the number of independent directions you can move in.
  - **2D** = a flat surface (length & width). A "ball" in 2D is a circle.
  - **3D** = our everyday world (length, width, height). A "ball" in 3D is a sphere.
  - **4D, 5D, … 31D** = mathematical spaces with 4, 5, … 31 independent directions. We cannot see or draw them, but the geometry is well-defined.
- On the x-axis of the diagram, **"Dimension n"** means we are asking the kissing number question in n-dimensional space.

### What is the "kissing number"?

- The kissing number in dimension n, written **K(n)**, is the **maximum number of non-overlapping unit balls that can all touch one central unit ball** in n-dimensional space.
- "Kissing" = touching. So yes, **kissing number = maximum number of touching spheres**.
- Examples: K(1)=2, K(2)=6, K(3)=12, K(4)=24, K(8)=240, K(24)=196,560.
- In most dimensions we only know a range: a **lower bound** ("at least this many") and an **upper bound** ("at most this many"). PackingStar improves the lower bound — it finds valid arrangements with more spheres than anyone had before.

---

## Panel-by-panel explanation

### Left panel (main chart): Standard kissing numbers, dimensions 11–31

| Element | Meaning |
|---|---|
| **Grey line + dots** | Previously known best lower bounds for each dimension n (the "at least" record before PackingStar). |
| **Blue triangle** (11D) | The 11D improvement by AlphaEvolve (Google DeepMind, 2025): K(11)=593. A different AI system that also worked on this problem. |
| **Red stars** | PackingStar's new records. Each star sits above the grey line, showing it beat the old record. |
| **Y-axis (log scale)** | The kissing number itself (how many spheres). It uses a logarithmic scale because the numbers grow enormously — from ~600 in 11D to ~300,000 in 31D. |
| **Inset bar chart** | Shows **ΔK(n) = K_new(n) − K_prev(n)** for dimensions 25–31. This is how many *extra* spheres PackingStar found compared to the old record. The improvement grows dramatically with dimension: +8 in 25D, +38 in 26D, up to +5476 in 31D. |

**Specific callouts on the chart:**

- **K_new(25) = 197,056** — labelled "conjectured optimal, prev. 2016." This means PackingStar's 25D result may actually be the true kissing number (not just a lower bound), though this has not been formally proven.
- **K(11) = 593, prev. 2022** — AlphaEvolve's result (blue triangle), not PackingStar.
- **K_r(13) = 1146, rational advance over 1971** — This is a special kind of advance (see "rational vs non-rational" below). The subscript "r" means "rational." The current best *overall* is K(13) = 1154, but that uses non-rational coordinates.

### Right panel: Generalised kissing numbers

This is a **different, stricter** version of the problem. Instead of just requiring that spheres don't overlap (cosine between centres ≤ 1/2), it imposes a **tighter angular constraint** — for example, cosine ≤ 1/3 or cosine ≤ 1/4.

| Red star | Meaning |
|---|---|
| K_new(12, 1/4) = 81 | In 12D, under the 1/4-cosine constraint, PackingStar found 81 spheres. |
| K_new(14, 1/3) = 252, prev. 2024 | In 14D with 1/3 constraint, 252 spheres (beating the 2024 record). |
| K_new(17, 1/3) = 578, prev. 2001 | In 17D with 1/3 constraint, 578 spheres (beating a 2001 record). |
| K_new(20, 1/4) = 405, prev. 2001 | In 20D with 1/4 constraint, 405 spheres. |
| K_new(21, 1/4) = 567, prev. 1995 | In 21D with 1/4 constraint, 567 spheres (beating a record from 1995). |

The grey line shows previously known generalised kissing numbers.

---

## Rational vs. non-rational: what's the difference?

This distinction matters especially in **13 dimensions**.

### What "rational" means here

- Each sphere configuration can be described by a **cosine matrix** — a table of angles between every pair of sphere centres.
- If **every entry** in that table is a **rational number** (a fraction like 1/2, −1/3, 0), the configuration is called **rational**.
- If some entries are **irrational** (like √2/3 or values that cannot be expressed as fractions), it's **non-rational**.

### Why it matters

| | Rational | Non-rational |
|---|---|---|
| **Cosine values** | All are exact fractions (e.g. 1/2, 0, −1/3) | Some involve irrational numbers |
| **Mathematical study** | Can be analysed exactly, no rounding errors | Requires numerical approximations |
| **Practical use** | Easier for coding/decoding in communications | Harder to implement precisely |
| **Current 13D records** | **K_r(13) = 1146** (PackingStar, new!) | K(13) = 1154 (since 1999) |
| **Previous 13D rational** | 1130 (since 1971 — unchanged for 50+ years!) | — |

### The 13D story

- Since 1971, the best known **rational** configuration in 13D had 1130 spheres.
- In 1999, someone found a **non-rational** configuration with 1154 spheres by slightly adjusting coordinates.
- PackingStar achieved **1146 rational spheres** — breaking the 50-year rational record for the first time!
- 1146 is still below the non-rational 1154, but the rational result is valuable: it allows exact mathematical analysis and is more useful for practical applications like error-correcting codes.
- This is why the chart says **"K_r(13) = 1146, rational advance over 1971"** and notes **"current best: K(13) = 1154 but non-rational."**

### In other dimensions

In dimensions 25–31, the distinction is less prominent — the new records are simply the best known lower bounds of any type.

---

## Summary

The diagram tells a story of **scale and scope**:
- **Across 7 dimensions** (25–31), PackingStar beats every previous record, with improvements growing from +8 to +5476 spheres.
- **In 13D**, it breaks a 50-year rational record.
- **For generalised kissing numbers** (stricter constraints), it beats records in 5 settings, some dating back to the 1990s.
- All results are independently verified and accepted into official mathematical databases.
