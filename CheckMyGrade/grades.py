import csv
import statistics

class Grades:
    def __init__(self):
        self.students_file = 'data\\students.csv'
        self.professors_file = 'data\\professors.csv'

    def load_grades(self):
        grades_data = []
        try:
            with open(self.students_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    grades_data.append({
                        'student_id': row['student_id'],
                        'course_id': row['course_id'],
                        'score': float(row['score']),
                        'professor_id': row['professor_id']
                    })
        except FileNotFoundError:
            print(f"File {self.students_file} not found.")
        return grades_data

    def display_grade_report(self):
        with open(self.students_file, 'r') as file:
            reader = csv.DictReader(file)
            print("\n📊 Grade Report")
            for row in reader:
                print(f"Email: {row['Email']}, Course ID: {row['Course ID']}, Marks: {row['Marks']}, Grade: {self.calculate_grade(int(row['Marks']))}")

    def get_course_scores(self, course_id):
        scores = [entry['score'] for entry in self.grades_data if entry['course_id'] == course_id]
        return scores

    def average_score(self, course_id):
        scores = []
        with open(self.students_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Course ID'] == course_id:
                    scores.append(float(row['Marks']))
        if scores:
            return sum(scores) / len(scores)
        return None

    def median_score(self, course_id):
        scores = []
        with open(self.students_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Course ID'] == course_id:
                    scores.append(float(row['Marks']))
        if scores:
            return statistics.median(scores)
        return None

    def generate_professor_report(self, professor_id):
        """Generate a report showing all students and grades assigned to a professor."""
        professor_name = None
        course_id = None

        # 🔍 Step 1: Find the Professor's Name and Course ID
        with open(self.professors_file, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Professor ID'].strip().lower() == professor_id.strip().lower():  
                    professor_name = row['Name']
                    course_id = row['Course ID']
                    break  

        if not professor_name or not course_id:
            return {"error": "Professor not found", "Students": []}  # ✅ Always return "Students"

        # 🔍 Step 2: Fetch Students Enrolled in This Course
        students_found = []
        with open(self.students_file, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Course ID'].strip() == course_id.strip():
                    students_found.append({
                        "Student Email": row['Email'],
                        "Marks": row['Marks'],
                        "Grade": row['Grade']
                    })

        # ✅ Always return structured data
        return {
            "Name": professor_name,
            "Course ID": course_id,
            "Students": students_found
        }
    
    def calculate_grade(self, marks):
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
