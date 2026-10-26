def calculate_grades(*marks, **student):
    if not marks:
        return None

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return (
        student.get("name", "Unknown"),
        min(marks),
        max(marks),
        average,
        grade
    )


name = input("Enter student name: ")
marks = list(map(
    float,
    input("Enter marks separated by spaces: ").split()
))

try:
    result = calculate_grades(*marks, name=name)

    if result:
        name, minimum, maximum, average, grade = result

        print("\nStudent:", name)
        print("Minimum marks:", minimum)
        print("Maximum marks:", maximum)
        print("Average:", round(average, 2))
        print("Grade:", grade)

except ValueError as e:
    print("Error:", e)