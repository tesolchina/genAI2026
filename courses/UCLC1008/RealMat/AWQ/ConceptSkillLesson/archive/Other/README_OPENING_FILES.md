# Opening lesson files

Some systems or apps (e.g. OneDrive, certain editors, scripts) may fail to open files whose names contain **spaces** or **parentheses**.

**If a file does not open**, use the **safe-filename** version below:

| Original filename | Safe-filename copy (use this if the original won’t open) |
|-------------------|-----------------------------------------------------------|
| `UCLC1008 (2526a) Sample AWQ (Student).md` | `UCLC1008_2526a_Sample_AWQ_Student.md` |

The content of the two files is the same. The underscore version is kept in sync for compatibility.

**PDF:** If you have a PDF with a long hash in the name (e.g. `..._1ea7ccd76d29f173ef90c4263cd6ad72.pdf`) and it will not open, try opening it from a local folder (not via sync) or rename it to a shorter name, e.g. `UCLC1008_2526a_Sample_AWQ_Student.pdf`.

**"Unable to open" / "Argument is undefined or null":** If `10task_revision_plan.md` fails to open (e.g. in Cursor/VS Code), use the same content under the new name: **`lessons/Plans/revision_plan_10tasks.md`**. Filenames that start with a number can trigger this error in some editors.
