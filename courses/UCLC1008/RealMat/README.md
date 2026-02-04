# RealMat — organised course materials (UCLC1008)

This folder is a **curated copy** of materials from the parent course folder, organised by assessment and type. **Original folders and file paths are unchanged** (so existing prompts that reference them still work).

## Structure

- **AWQ** — Academic Writing Quiz (Weeks 1–6)
- **ACE** — Argumentation Construction and Evaluation (Weeks 6–9)
- **CRAA** — Critical Reading and Argument Analysis (Weeks 10–13)

Under each area:

| Subfolder | Contents |
|-----------|----------|
| **FromCourseTeam** | Official instructions, rubrics, modules, calendar |
| **ExamTipsPractice** | Sample tasks, student answers, study guides, mock practice |
| **ConceptSkillLesson** | Lesson plans, weekly plans, Moodle tasks, concept/skill materials |

### AWQ second layer (easier to locate files)

Under **AWQ**, each of the three subfolders above is split into a second layer:

| Layer1 | Layer2 subfolders |
|--------|-------------------|
| **FromCourseTeam** | `Instructions` · `Modules` · `RubricsAndCalendar` |
| **ExamTipsPractice** | `Samples` · `StudyGuides` · `MockPractice` |
| **ConceptSkillLesson** | `WeeklyPlans` · `LessonContent` · `MoodleTasks` · `ReadingAndSynthesis` · `Other` |

See **AWQ/LAYER2_MAP.md** for what goes where. After re-running `populate_from_inventory.py`, run **AWQ/organize_layer2.py** to sort files into the second layer again.

## Counts (current)

- AWQ: 109 files (in second-layer subfolders)  
- ACE: 9 files  
- CRAA: 5 files

## Maintenance

- **INVENTORY.md** — Master list: each source path and its (Area, Subfolder). Edit this to add/move/remove items, then run `python3 populate_from_inventory.py` to refresh the copy.
- **populate_from_inventory.py** — Copies files from the course folder into `RealMat/<Area>/<Subfolder>/`. Duplicate basenames get a path-based prefix (e.g. `materials_course_materials_in_MD_Sample AWQ.md`).
