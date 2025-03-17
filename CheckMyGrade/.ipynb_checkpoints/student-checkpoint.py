import csv
import os
from grades import Grades

class Student:
    def __init__(self, email=None, first_name=None, last_name=None, course_id=None, marks=None, student_file='data\\students.csv'):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.marks = marks
        self.student_file = student_file
        self.grades = Grades()
        self.grade = self.grades.calculate_grade(marks) if marks is not None else None  # Auto-assign grade if marks is provided

class StudentManager:
    def __init__(self, file_path='data\\students.csv'):
        self.file_path = file_path
        # Create the data directory if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        # Create the CSV file with headers if it doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Grade", "Marks"])

    def load_students(self):
        students = []
        if os.path.exists(self.file_path):
            print(f"Loading students from {self.file_path}...")  # Debug print
            with open(self.file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header row
                for row in reader:
                    print(f"Read row: {row}")  # Debug print
                    if len(row) == 6:  # Ensure correct number of columns
                        students.append(Student(row[0], row[1], row[2], row[3], row[5]))  # Ignore old grade
        else:
            print(f"File {self.file_path} does not exist.")  # Debug print
        return students

    def save_students(self, students):
        print(f"Saving students to {self.file_path}...")  # Debug print
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Grade", "Marks"])
            for student in students:
                print(f"Writing student: {student.email}, {student.first_name}, {student.last_name}, {student.course_id}, {student.grade}, {student.marks}")  # Debug print
                writer.writerow([student.email, student.first_name, student.last_name, student.course_id, student.grade, student.marks])

    def add_student(self, email, first_name, last_name, course_id, marks):
        try:
            grade = Grades().calculate_grade(marks)
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([email, first_name, last_name, course_id, grade, marks])
            print("✅ Student added successfully!")
        except Exception as e:
            print(f"❌ Error adding student: {e}")

    def delete_student(self, email, course_id):
        try:
            rows = []
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)
                rows.append(header)
                for row in reader:
                    if not (row[0] == email and row[3] == course_id):
                        rows.append(row)
            
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("✅ Student deleted successfully!")
        except Exception as e:
            print(f"❌ Error deleting student: {e}")

    def modify_student(self, email, course_id, first_name=None, last_name=None, marks=None):
        try:
            rows = []
            modified = False
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)
                rows.append(header)
                for row in reader:
                    if row[0] == email and row[3] == course_id:
                        if first_name:
                            row[1] = first_name
                        if last_name:
                            row[2] = last_name
                        if marks:
                            row[5] = marks
                            row[4] = Grades().calculate_grade(marks)
                        modified = True
                    rows.append(row)
            
            if modified:
                with open(self.file_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print("✅ Student modified successfully!")
            else:
                print("❌ Student not found!")
        except Exception as e:
            print(f"❌ Error modifying student: {e}")

    def check_my_grades(self, email):
        return self._get_student_data(email, grade=True)

    def check_my_marks(self, email):
        return self._get_student_data(email, grade=False)

    def _get_student_data(self, email, grade=True):
        try:
            with open(self.file_path, mode='r') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Skip header row
                results = []
                
                for row in csv_reader:
                    # Verify row has all required fields
                    if len(row) >= 6 and row[0] == email:
                        try:
                            if grade:
                                marks = int(row[5]) if row[5] else 0
                                calculated_grade = self._calculate_grade(marks)
                                result = f"Course ID: {row[3]}, Grade: {calculated_grade}"
                            else:
                                result = f"Course ID: {row[3]}, Marks: {row[5]}"
                            results.append(result)
                        except (ValueError, IndexError) as e:
                            print(f"Warning: Invalid data for student {email}: {e}")
                            continue
                
                if not results:
                    print(f"No records found for student with email: {email}")
                return results if results else None
                
        except FileNotFoundError:
            print(f"Error: Cannot find {self.file_path}")
            return None
        except Exception as e:
            print(f"Error reading student data: {str(e)}")
            return None

    def _calculate_grade(self, marks):
        try:
            marks = int(marks)
            if marks >= 90:
                return 'A'
            elif marks >= 80:
                return 'B'
            elif marks >= 70:
                return 'C'
            elif marks >= 60:
                return 'D'
            else:
                return 'F'
        except (ValueError, TypeError):
            return 'N/A'

    def display_students(self):
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                print("\n📚 **Student List**")
                print("-" * 70)
                print(f"{'Email':<25} {'First Name':<12} {'Last Name':<12} {'Course ID':<10} {'Grade':<6} {'Marks':<6}")
                print("-" * 70)
                for row in reader:
                    print(f"{row[0]:<25} {row[1]:<12} {row[2]:<12} {row[3]:<10} {row[4]:<6} {row[5]:<6}")
                print("-" * 70)
        except FileNotFoundError:
            print("❌ No student records found.")
        except Exception as e:
            print(f"❌ Error displaying students: {e}")