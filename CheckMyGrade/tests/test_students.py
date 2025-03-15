import unittest
import csv
import os
import time
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Move up one directory level
from student import StudentManager

class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        """Create a student file with 1000 records for testing."""
        self.test_file = "data/test_students.csv"
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)
        
        with open(self.test_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "First Name", "Last Name", "Course ID", "Grade", "Marks"])  # Header
            for i in range(1000):
                writer.writerow([f"student{i}@mail.com", f"First{i}", f"Last{i}", "101", "B", str(50 + i % 50)])

        self.student_manager = StudentManager(self.test_file)  # Create an instance of StudentManager with test file

    def tearDown(self):
        """Remove the test file after testing."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_students(self):
        """Test adding 1000 students and measure time."""
        start_time = time.time()
        for i in range(1000, 2000):
            self.student_manager.add_student(f"student{i}@mail.com", f"First{i}", f"Last{i}", "102", str(60 + i % 40))
        elapsed_time = time.time() - start_time
        print(f"✅ Time taken to add 1000 students: {elapsed_time:.5f} seconds")
    
    def test_delete_students(self):
        """Test deleting 1000 students and measure time."""
        start_time = time.time()
        for i in range(500, 1500):  # Deleting 1000 existing students
            self.student_manager.delete_student(f"student{i}@mail.com", "101")
        elapsed_time = time.time() - start_time
        print(f"✅ Time taken to delete 1000 students: {elapsed_time:.5f} seconds")
    
    def test_modify_students(self):
        """Test modifying 1000 students and measure time."""
        start_time = time.time()
        for i in range(100, 1100):
            self.student_manager.modify_student(f"student{i}@mail.com", "101", first_name=f"Updated{i}")
        elapsed_time = time.time() - start_time
        print(f"✅ Time taken to modify 1000 students: {elapsed_time:.5f} seconds")

    def test_search_students(self):
        """Test searching 1000 students and measure time."""
        start_time = time.time()
        for i in range(500, 1500):
            self.student_manager.check_my_grades(f"student{i}@mail.com")
        elapsed_time = time.time() - start_time
        print(f"✅ Time taken to search 1000 students: {elapsed_time:.5f} seconds")

if __name__ == "__main__":
    unittest.main()
