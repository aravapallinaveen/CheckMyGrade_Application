import unittest
import csv
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Move up one directory level
from student import Student

class TestSorting(unittest.TestCase):
    """Unit tests for sorting students."""

    def setUp(self):
        """Set up test data with a few student records and ensure the test file is used for each test case."""
        self.test_file = "data/test_students.csv"  # Use a temporary test file
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)

        with open(self.test_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Marks"])  # Header
            writer.writerow(["student1@mail.com", "First1", "Last1", "101", 85])
            writer.writerow(["student2@mail.com", "First2", "Last2", "102", 90])
            writer.writerow(["student3@mail.com", "First3", "Last3", "103", 75])

        self.original_file = Student.__dict__.get("STUDENT_FILE", None)
        Student.STUDENT_FILE = self.test_file  # Override global file path

    def tearDown(self):
        """Remove the test file and restore the original file path."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if self.original_file:
            Student.STUDENT_FILE = self.original_file

    def load_students(self):
        """Helper function to read students from CSV"""
        students = []
        with open(self.test_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 5:  # Ensure row has enough columns
                    students.append(Student(row[0], row[1], row[2], row[3], int(row[4])))  # Convert marks to int
        return students

    def test_sort_by_marks(self):
        students = self.load_students()
        start_time = time.time()
        sorted_students = sorted(students, key=lambda s: s.marks, reverse=True)
        elapsed_time = time.time() - start_time

        self.assertTrue(all(sorted_students[i].marks >= sorted_students[i + 1].marks for i in range(len(sorted_students) - 1)))
        print(f"✅ Sorting by marks took {elapsed_time:.5f} seconds")

    def test_sort_by_email(self):
        students = self.load_students()
        start_time = time.time()
        sorted_students = sorted(students, key=lambda s: s.email)
        elapsed_time = time.time() - start_time

        self.assertTrue(all(sorted_students[i].email <= sorted_students[i + 1].email for i in range(len(sorted_students) - 1)))
        print(f"✅ Sorting by email took {elapsed_time:.5f} seconds")

if __name__ == "__main__":
    unittest.main()
