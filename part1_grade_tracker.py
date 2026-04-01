# Raw student data (given)
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "   Priya Nair   ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Store cleaned data
cleaned_students = []

# Loop through each student
for student in raw_students:

    # Clean name
    name = student["name"].strip().title()

    # Convert roll number
    roll = int(student["roll"])

    # Convert marks string to list of integers
    marks_list = student["marks_str"].split(",")
    marks = []

    for mark in marks_list:
        marks.append(int(mark.strip()))

    # Create cleaned student dictionary
    clean_student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    cleaned_students.append(clean_student)

    # Validate name
    is_valid = all(word.isalpha() for word in name.split())

    if is_valid:
        print(f"{name} ✓ Valid name")
    else:
        print(f"{name} ✗ Invalid name")

    # Print profile card
    print("=" * 35)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 35)


# Find student with roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print(student["name"].upper())
        print(student["name"].lower())


# ---------------- TASK 2 ----------------

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\n--- Marks Analysis ---")

for i in range(len(subjects)):
    subject = subjects[i]
    mark = marks[i]

    # Assign grade
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject}: {mark} → {grade}")

# Total marks
total = sum(marks)

# Average marks
average = total / len(marks)

# Highest scoring subject
max_mark = max(marks)
max_index = marks.index(max_mark)
highest_subject = subjects[max_index]

# Lowest scoring subject
min_mark = min(marks)
min_index = marks.index(min_mark)
lowest_subject = subjects[min_index]

print("\n--- Summary ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Highest: {highest_subject} ({max_mark})")
print(f"Lowest: {lowest_subject} ({min_mark})")

# Adding new subjects
new_count = 0

while True:
    subject = input("\nEnter subject name (or type 'done' to stop): ")

    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    # Validate input
    if not mark_input.isdigit():
        print("Invalid input! Marks must be a number.")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print("Invalid input! Marks must be between 0 and 100.")
        continue

    # Add valid data
    subjects.append(subject)
    marks.append(mark)
    new_count += 1

# Updated results
updated_total = sum(marks)
updated_average = updated_total / len(marks)

print("\n--- Updated Results ---")
print(f"New subjects added: {new_count}")
print(f"Updated Average: {updated_average:.2f}")


# ---------------- TASK 3 ----------------

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85]),
]

print("\n--- Class Report ---")
print(f"{'Name':<15} | {'Average':<7} | Status")
print("-" * 40)

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0

total_class_avg = 0

for name, marks in class_data:
    avg = sum(marks) / len(marks)

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    total_class_avg += avg

    print(f"{name:<15} | {avg:>6.2f} | {status}")

class_average = total_class_avg / len(class_data)

print("\n--- Summary ---")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Topper: {topper_name} ({topper_avg:.2f})")
print(f"Class Average: {class_average:.2f}")
