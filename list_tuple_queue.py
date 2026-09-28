##list
student_names = ["Ahmed", "Sara", "Omar", "Fatima", "Ali"]
student_ages = [20, 21, 19, 22, 20]
ai_students = ["Ahmed", "Omar", "Ali"]

#tuple
ahmed = ("S101", "Ahmed", 20, "AI")
sara = ("S102", "Sara", 21, "Computer Science")

#queue
from collections import deque

registration_queue = deque(["Ahmed", "Sara", "Omar"])

registration_queue.append("Fatima")
registration_queue.popleft()
print(registration_queue)