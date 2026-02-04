#!/usr/bin/env python3
"""Move AWQ files from Layer1 (FromCourseTeam, ExamTipsPractice, ConceptSkillLesson) into Layer2 subfolders."""
import shutil
from pathlib import Path

AWQ = Path(__file__).resolve().parent

def move(parent: str, rules: list[tuple[str, list[str]]]):
    """rules: list of (subfolder, [patterns]). Pattern is substring in filename."""
    base = AWQ / parent
    if not base.is_dir():
        return
    for f in base.iterdir():
        if not f.is_file():
            continue
        name = f.name
        for sub, patterns in rules:
            if any(p in name for p in patterns):
                dst = base / sub
                dst.mkdir(parents=True, exist_ok=True)
                shutil.move(str(f), str(dst / name))
                print(f"  {parent}/{name} -> {parent}/{sub}/")
                break

# FromCourseTeam
move("FromCourseTeam", [
    ("Instructions", ["Academic Writing Quiz Instructions", "Pre-course Writing Instructions", "emailFromCourseCoordinator"]),
    ("Modules", ["Module 1", "Module 2", "UE1 (2526B) Module"]),
    ("RubricsAndCalendar", ["Rubrics_Plain", "Academic_Calendar"]),
])

# ExamTipsPractice
move("ExamTipsPractice", [
    ("Samples", ["Sample Academic Writing Quiz", "UCLC1008", "Sample AWQ"]),
    ("StudyGuides", ["Study Guide", "StudyGuideAWQ"]),
    ("MockPractice", ["practice1", "wordCountSampleQuiz", "setQuestion"]),
])

# ConceptSkillLesson
move("ConceptSkillLesson", [
    ("WeeklyPlans", ["plan_week", "planAWQ", "plan15", "originalPlanAWQ", "revisePlan", "materials_Week1-5_AWQ", "lessons_Plans_week"]),
    ("LessonContent", ["week1.", "week2.", "week3.", "week4.", "week5."]),
    ("MoodleTasks", ["task1", "task2", "W3H1_", "W3H3_", "README_W3H1", "README_W3H3"]),
    ("ReadingAndSynthesis", [
        "AIagentDemo_MockPractice_JumpWaterAgain", "Xie2023", "Skjuve2021", "LiZhang2024", "Laestadius2022", "XiePentina2022",
        "context.md", "extractFilterRef", "focusReading", "taskOrientation", "understandTask",
        "detailedPlan", "detailedplan02", "synthesisPlan", "linearPoints", "prep.md", "commentsonLinear",
        "enhanceDetailedPlan", "visualize", "guide_game_FRT", "jumpWaterAgain", "Ho2025",
    ]),
    ("Other", ["README_OPENING", "README.md", "detailedLessons15", "sampleLessonbuild", "sample_paraphrasing", "InputProcessOutputModel"]),
])

# LessonContent: also week1.md, week2.md, ... (no dot) — move from ConceptSkillLesson root if still there
csl = AWQ / "ConceptSkillLesson"
for f in list(csl.iterdir()):
    if not f.is_file():
        continue
    if f.name in ("week1.md", "week2.md", "week3.md", "week4.md", "week5.md"):
        dst = csl / "LessonContent"
        shutil.move(str(f), str(dst / f.name))
        print(f"  ConceptSkillLesson/{f.name} -> ConceptSkillLesson/LessonContent/")

print("Done.")
