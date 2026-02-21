# Coursera AI – Expense Tracker (Cursor Edition)

This folder contains the **Coursera / Vanderbilt** exercise *“Getting Started with Claude Code & Building Your First Application”* re-run **in Cursor** instead of Claude Code. The same “big prompt” was used to build a full expense tracking app here.

---

## What Was Accomplished

- **Project setup**  
  Next.js 14 (App Router), TypeScript, and Tailwind CSS in `expense-tracker/`.

- **Core features**
  - **Add expenses** with date, amount, category, and description.
  - **View expenses** in a table with clear layout.
  - **Filter** by date range and category; **search** by description.
  - **Dashboard** with:
    - Total spending (respecting current filters).
    - This month’s spending.
    - Top categories.
  - **Spending by category** shown as a simple bar chart.

- **Data & UX**
  - **Persistence** via `localStorage` (no backend).
  - **Categories**: Food, Transportation, Entertainment, Shopping, Bills, Other.
  - **Edit** and **delete** existing expenses.
  - **Export** all expenses to CSV.
  - **Form validation** (required date, positive amount, required description).
  - **Currency formatting** (USD) and **date picker** for expense date.
  - **Responsive** layout and basic loading/feedback (e.g. “Expense added”, “CSV exported”).

- **Run instructions**
  - From repo root: `cd courses/courseraAI/expense-tracker && npm run dev`
  - Open **http://localhost:3000** and use the app.

---

## What to Learn From This

1. **“Big prompt” workflow**  
   One detailed prompt (see `prompt.md`) was enough to get a full app: features, tech stack, and UX. The same idea from the course (vision-level instructions instead of tiny steps) works in Cursor.

2. **Stack in practice**  
   - **Next.js 14 App Router** for routing and layout.  
   - **TypeScript** for types (`Expense`, `Category`, etc.) and safer refactors.  
   - **Tailwind** for layout, cards, forms, and responsive design.  
   - **Client-only data**: `"use client"` + `useEffect` for loading/saving from `localStorage` and avoiding hydration issues.

3. **State and persistence**  
   - React state for form, filters, and list.  
   - Sync to `localStorage` on change so data survives refresh.  
   - Filtering is derived state (no duplicate storage).

4. **UX details**  
   - Validation before submit.  
   - Edit mode (prefill form, Update/Cancel).  
   - Short success messages.  
   - Empty state when no expenses match filters.

5. **No backend**  
   Everything is client-side and demo-friendly; swapping `localStorage` for an API later would follow the same component structure.

---

## Files You Care About

| Path | Purpose |
|------|--------|
| `prompt.md` | The “big prompt” used to build the app. |
| `moduleInfo.md` | Course module text (Claude Code setup, big prompts, etc.). |
| `task.md` | Original task: review info/prompt, run in Cursor, add this README. |
| `expense-tracker/` | Full Next.js app (see `expense-tracker/README.md` for run commands). |

---

## Running the App

```bash
cd courses/courseraAI/expense-tracker
npm install   # if you haven’t already
npm run dev
```

Then open **http://localhost:3000** and add/filter/edit/export expenses.
