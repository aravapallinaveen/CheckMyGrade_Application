import csv
import os

class Course:
    def __init__(self, course_id, course_name, description, course_file="data\\courses.csv"):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.course_file = course_file

    def load_courses(self):
        courses = []
        if os.path.exists(self.course_file):
            with open(self.course_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header row
                course_data = list(reader)  # Read all rows before closing

        for row in course_data:  # Process data after closing the file
            if len(row) == 3:  # Ensure correct number of columns
                courses.append(Course(row[0], row[1], row[2], self.course_file))
            else:
                print(f"⚠ Skipping invalid row: {row}")  
        return courses

    def save_courses(self, courses):
        with open(self.course_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Course ID", "Course Name", "Description"])
            for course in courses:
                writer.writerow([course.course_id, course.course_name, course.description])

    def add_course(self, course_id, course_name, description):
        courses = self.load_courses()

        # Check for duplicate Course ID
        if any(course.course_id == course_id for course in courses):
            print("⚠ Course with this ID already exists!")
            return

        courses.append(Course(course_id, course_name, description, self.course_file))
        self.save_courses(courses)
        print("✅ Course added successfully!")

    def delete_course(self, course_id):
        courses = self.load_courses()
        filtered_courses = [c for c in courses if c.course_id != course_id]

        if len(courses) == len(filtered_courses):
            print("⚠ Course not found!")
            return

        self.save_courses(filtered_courses)
        print("✅ Course deleted successfully!")

    def modify_course(self, course_id, course_name=None, description=None):
        courses = self.load_courses()
        modified = False

        for course in courses:
            if course.course_id == course_id:
                if course_name: course.course_name = course_name
                if description: course.description = description
                modified = True
                break

        if not modified:
            print("⚠ Course not found!")
            return

        self.save_courses(courses)
        print("✅ Course updated successfully!")

    def display_courses(self):
        courses = self.load_courses()
        if not courses:
            print("No courses available!")
            return

        print("\nCourse List:")
        print("------------------------------------------------------")
        print(f"{'Course ID':<10}{'Course Name':<25}{'Description'}")
        print("------------------------------------------------------")

        for course in courses:
            print(f"{course.course_id:<10}{course.course_name:<25}{course.description}")

        print("------------------------------------------------------")


