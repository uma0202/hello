from collections import deque

# Scalars: str, int, float, bool
name = "Ahmed"
batch = "Super30-2026"
course = "Artificial Intelligence"
learning_goal = "Build ML projects and land an internship"
is_active = True
last_sem_gpa = 8.75

# String
header = f"{name} | {batch} | {course}"
print(header)
print("-" * len(header))

# Tuple — fixed ID record
record = ("S101", 2026, "A")

# List — courses this semester
courses = ["Python", "Data Structures", "Machine Learning"]

# Dict — profile + nested marks
student = {
    "name": name,
    "batch": batch,
    "course": course,
    "learning_goal": learning_goal,
    "is_active": is_active,
    "last_sem_gpa": last_sem_gpa,
    "record": record,
    "courses": courses,
    "last_sem_marks": {
        "Python": 88,
        "Math": 92,
        "AI": 85,
    },
}

# Set — unique interests
student["interests"] = {"ML", "Open Source", "Chess", "ML"}

# Frozenset — fixed core skills
core_skills = frozenset({"Python", "Git", "Problem Solving"})

# Queue (deque)
queue = deque([name, "Sara"])
served = queue.popleft()

# Output
print("Name:", student["name"])
print("Batch:", student["batch"])
print("Course:", student["course"])
print("Learning goal:", student["learning_goal"])
print("Active:", student["is_active"])
print("Record (tuple):", student["record"])
print("Courses (list):", student["courses"])
print("Interests (set):", student["interests"])
print("Core skills (frozenset):", core_skills)
print("Last sem marks (dict):")
for subject, mark in student["last_sem_marks"].items():
    print(f"  {subject}: {mark}")
avg = sum(student["last_sem_marks"].values()) / len(student["last_sem_marks"])
print(f"Average (float): {avg:.2f}, GPA: {student['last_sem_gpa']}")
print("Queue served first:", served, "| Remaining:", list(queue))