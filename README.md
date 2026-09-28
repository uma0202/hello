# **Different Python data structures:**
Set : A set is an unordered collection of unique values.
Characteristics:

Unordered
Mutable, meaning object can be changed after it has been created.
Does not allow duplicates
Does not support normal indexing
Written using {}

Dictionary: A dictionary stores data as key-value pairs.
Characteristics:
Stores key-value pairs
Mutable
Keys must be unique
Accessed using keys
Written using {}


| Dictionary                   | Set                            |
| ---------------------------- | ------------------------------ |
| Stores **key-value pairs**   | Stores **unique values**       |
| Uses `{key: value}`          | Uses `{value1, value2}`        |
| Used to describe information | Used to represent unique items |
| `student["name"]`            | `"Python" in skills`           |

 # **String Data Structure**

- A string is a sequence of characters. The Python data type for strings is str.
- It is used to store text in Python.
- Strings are written inside single (' ') or double (" ") quotes.
   example = "Hello World"
- Python strings are immutable, meaning their characters cannot be changed directly.
- Common string methods include:
   upper() – converts to uppercase
   lower() – converts to lowercase
   replace() – replaces text
   split() – splits a string
   strip() – removes extra spaces
   len()- gives length of the string 

# List, Tuple, and Queue Examples

Data structures are used to store and organize information. Below are simple real-world examples using dummy student data.

## 1. List

A **list** stores multiple items in an ordered and changeable collection.

### Example 1: Student Names

```python
student_names = ["Ahmed", "Sara", "Omar", "Fatima", "Ali"]
```

### Example 2: Student Ages

```python
student_ages = [20, 21, 19, 22, 20]
```

### Example 3: AI Students

```python
ai_students = ["Ahmed", "Omar", "Ali"]
```

Lists are useful when the data may need to be added, removed, or changed.

---

## 2. Tuple

A **tuple** stores multiple items in an ordered collection that cannot be changed after creation.

### Example 1: Ahmed's Information

```python
ahmed = ("S101", "Ahmed", 20, "AI")
```

### Example 2: Sara's Information

```python
sara = ("S102", "Sara", 21, "Computer Science")
```

### Example 3: Omar's Information

```python
omar = ("S103", "Omar", 19, "Data Science")
```

Tuples are useful for storing information that should remain unchanged.

---

## 3. Queue

A **queue** follows the **FIFO (First In, First Out)** principle. The student who joins the queue first is served first.

### Example 1: Registration Queue

```python
from collections import deque

registration_queue = deque(["Ahmed", "Sara", "Omar"])
```

### Example 2: Exam Queue

```python
exam_queue = deque(["Ali", "Fatima", "Omar"])
```

### Example 3: Advisor Queue

```python
advisor_queue = deque(["Ahmed", "Omar", "Ali"])
```

Queues are useful for situations where students need to be served in the order they arrive.

---

## Conclusion

Lists, tuples, and queues are useful for organizing student information:

* **List:** Ordered and changeable data.
* **Tuple:** Ordered data that should not be changed.
* **Queue:** Data processed in **First In, First Out (FIFO)** order.

# Python Variables

- A **variable** is a name that refers to a value/object.
- Variables are created using `=`:
  ```python
  age = 20
  name = "Ali"

- Python automatically determines the data type:

int → 20
float → 19.99
str → "Ali"
bool → True

Variable names:
Can contain letters, numbers, and _
Cannot start with a number
Cannot contain - or spaces
Are case-sensitive
Python variables are names bound to objects, rather than traditional containers holding values.
