import csv
import os

STUDENT_FILE = "data\\students.csv"
COURSE_FILE = "data\\courses.csv"
PROFESSOR_FILE = "data\\professors.csv"

class Grades:
    def calculate_grade(self, marks):
        """Converts numerical marks into a letter grade."""
        try:
            marks = float(marks)
            if marks >= 90:
                return "A"
            elif marks >= 80:
                return "B"
            elif marks >= 70:
                return "C"
            elif marks >= 60:
                return "D"
            else:
                return "F"
        except ValueError:
            return "F"

    def get_professor_details(self, course_id):
        """Fetches the professor's name and role for a given course ID."""
        if not os.path.exists(PROFESSOR_FILE):
            return "Unknown", "Unknown"

        with open(PROFESSOR_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 4 and row[3] == course_id:  # Ensure valid entry
                    return row[1], row[2]  # Professor Name, Role
        return "Unknown", "Unknown"

    def get_course_name(self, course_id):
        """Fetches the course name for a given course ID."""
        if not os.path.exists(COURSE_FILE):
            return "Unknown Course"

        with open(COURSE_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 2 and row[0] == course_id:  # Ensure valid entry
                    return row[1]  # Course Name
        return "Unknown Course"

    def is_numeric(self, value):
        """Checks if a value is numeric."""
        try:
            float(value)
            return True
        except ValueError:
            return False

    def display_grade_report(self):
        """Displays all student grades sorted in descending order of marks, including course & professor details."""
        if not os.path.exists(STUDENT_FILE):
            print("❌ No student records found.")
            return

        grades_list = []
        with open(STUDENT_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 6:  # Ensure valid row format
                    email, first_name, last_name, course_id, grade, marks = row[:6]
                    
                    if self.is_numeric(marks):
                        marks = float(marks)  # Convert to float
                    else:
                        print(f"❌ Invalid marks ({marks}) for {email}. Setting to 0.")
                        marks = 0.0  # Default invalid marks to 0.0

                    # Ensure grade is correct
                    calculated_grade = self.calculate_grade(marks)
                    if grade != calculated_grade:
                        grade = calculated_grade  # Correct grade if mismatch

                    professor_name, professor_role = self.get_professor_details(course_id)
                    course_name = self.get_course_name(course_id)

                    # Debugging print statements
                    print(f"DEBUG: {email}, {course_id}, {course_name}, {professor_name}, {professor_role}")

                    grades_list.append((email, first_name, last_name, course_id, course_name, marks, grade, professor_name, professor_role))

        # Sort by marks in descending order
        grades_list.sort(key=lambda x: x[5], reverse=True)

        print("\n📊 **Grade Report (Sorted by Marks - High to Low)**")
        print("-" * 110)
        print(f"{'Email':<25} {'Name':<20} {'Course ID':<10} {'Course Name':<25} {'Marks':<6} {'Grade':<5} {'Professor':<20} {'Role':<15}")
        print("-" * 110)

        for email, first_name, last_name, course_id, course_name, marks, grade, professor_name, professor_role in grades_list:
            print(f"{email:<25} {first_name + ' ' + last_name:<20} {course_id:<10} {course_name:<25} {marks:<6.2f} {grade:<5} {professor_name:<20} {professor_role:<15}")

if __name__ == "__main__":
    grades = Grades()
    grades.display_grade_report()
