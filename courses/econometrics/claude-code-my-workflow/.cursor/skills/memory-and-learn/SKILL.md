---
name: memory-and-learn
description: Read MEMORY.md at session start and apply [LEARN:tag] corrections; when the user corrects you, append [LEARN:category] wrong → right to MEMORY.md. Use when starting work on this project or when the user gives a correction to remember.
---

# Memory and [LEARN] Protocol

## At session start (or when user says "read memory")

1. If `MEMORY.md` exists in the project root, read it.
2. Apply all `[LEARN:...]` entries: avoid repeating past mistakes (citations, notation, style).
3. Mention briefly that MEMORY was loaded and any relevant constraints.

## When the user corrects you

1. Append one line to `MEMORY.md` in this format:
   ```text
   [LEARN:category] wrong → right
   ```
   Examples: `[LEARN:citation] Belloni (2014) → Belloni (2013)`, `[LEARN:notation] T_t → T_i`.
2. Keep categories short (e.g. citation, notation, path, style). Do not duplicate existing lines.

## Purpose

MEMORY.md acts as a persistent "error log" so future sessions avoid the same mistakes. Keep entries concise.
