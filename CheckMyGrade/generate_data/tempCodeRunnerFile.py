import csv
import random

STUDENT_FILE = "data/students.csv"

def get_letter_grade(marks):
    """Convert numeric marks to letter grades"""
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def generate_students(filename, total_records=1000, students_with_4_courses=250):
    """Generates a CSV file with student records including grades."""
    courses = ["101", "102", "103", "104"]  # Sample Course IDs
    records_generated = 0
    student_id = 0

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Marks", "Grade"])  # Updated header

        while records_generated < total_records:
            email = f"student{student_id}@mail.com"
            first_name = f"First{student_id}"
            last_name = f"Last{student_id}"
            
            if student_id < students_with_4_courses:
                num_courses = 4
            else:
                num_courses = 3

            student_courses = random.sample(courses, num_courses)

            for course_id in student_courses:
                if records_generated >= total_records:
                    break
                marks = random.randint(40, 100)
                grade = get_letter_grade(marks)
                writer.writerow([email, first_name, last_name, course_id, marks, grade])
                records_generated += 1

            student_id += 1

    print(f"✅ {total_records} student records generated in {filename}")

# Run the function
generate_students(STUDENT_FILE)
