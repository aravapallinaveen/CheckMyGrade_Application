import unittest
import csv
import time
import os
import sys

# Adjust the sys.path to include the directory containing the student module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from student import Student  # Assuming Student class is in student.py

class TestSearch(unittest.TestCase):
    """Unit tests for searching students."""

    def setUp(self):
        """Set up test data with 1000 student records and ensure the test file is used for each test case."""
        self.test_file = "data/test_students.csv"  # Use a temporary test file
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)

        with open(self.test_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Marks"])  # Header
            for i in range(1000):
                writer.writerow([f"student{i}@mail.com", f"First{i}", f"Last{i}", "101", 85 + i % 15])

        self.original_file = Student.__dict__.get("STUDENT_FILE", None)
        Student.STUDENT_FILE = self.test_file  # Override global file path

    def tearDown(self):
        """Remove the test file and restore the original file path."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if self.original_file:
            Student.STUDENT_FILE = self.original_file

    def search_student_by_email(self, email):
        start_time = time.time()  # Start timer
        with open(Student.STUDENT_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row and row[0] == email:  # Email is in column 0
                    end_time = time.time()  # End timer
                    print(f"✅ Student Found: {row}")
                    print(f"⏳ Search Time: {end_time - start_time:.6f} seconds")
                    return row
        end_time = time.time()  # End timer
        print(f"❌ Student with email {email} not found.")
        print(f"⏳ Search Time: {end_time - start_time:.6f} seconds")
        return None

    def test_search_existing_student(self):
        """Test case: Search for an existing student."""
        email = "student999@mail.com"  # Modify based on generated data
        result = self.search_student_by_email(email)
        self.assertIsNotNone(result, "Student should exist in the records.")

    def test_search_non_existent_student(self):
        """Test case: Search for a non-existent student."""
        email = "notfound@mail.com"
        result = self.search_student_by_email(email)
        self.assertIsNone(result, "Student should not exist in the records.")

    def test_search_1000_students(self):
        """Test searching for 1000 students and measure execution time."""
        total_time = 0
        for i in range(1000):
            email = f"student{i}@mail.com"
            start_time = time.time()
            self.search_student_by_email(email)
            total_time += time.time() - start_time

        print(f"\n⏳ Total Time for Searching 1000 Students: {total_time:.6f} seconds")

if __name__ == "__main__":
    unittest.main()
