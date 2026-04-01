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
