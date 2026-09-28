from collections import deque

# Variables
student_name = "Ahmed"
semester = 4
cgpa = 3.45

# String
course_name = "Artificial Intelligence"

# List
courses = [
    "Python Programming",
    "Artificial Intelligence",
    "Machine Learning",
    "Data Structures"
]

# Tuple
course_details = ("Artificial Intelligence", 4, "AI-204")

# Dictionary
student = {
    "name": student_name,
    "semester": semester,
    "cgpa": cgpa,
    "major": "Artificial Intelligence"
}

# Set
ai_topics = {
    "Machine Learning",
    "Neural Networks",
    "Computer Vision",
    "Machine Learning",
    "NLP"
}

# Queue
lab_queue = deque()

lab_queue.append("Ahmed")
lab_queue.append("Sara")
lab_queue.append("Omar")
lab_queue.append("Fatima")

# Display information
print("AI Bachelor's Student Information")
print("----------------------------------")

print("Name:", student["name"])
print("Semester:", student["semester"])
print("CGPA:", student["cgpa"])
print("Major:", student["major"])

print("\nCurrent Course:")
print(course_name)

print("\nCourses:")
print(courses)

print("\nCourse Details:")
print(course_details)

print("\nUnique AI Topics:")
print(ai_topics)

print("\nAI Lab Queue:")
print(lab_queue)

# Remove the first student from the queue
first_student = lab_queue.popleft()

print("\nStudent entering the lab:")
print(first_student)

print("\nRemaining Queue:")
print(lab_queue)