import unittest
import csv
import os
import sys
import time

# Adjust the sys.path to include the directory containing the course module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "CheckMyGrade")))

from course import Course

class TestCourseManagement(unittest.TestCase):
    """Unit tests for the Course class."""

    def setUp(self):
        """Set up test data with a few course records and ensure the test file is used for each test case."""
        self.test_file = "data/test_courses.csv"  # Use a temporary test file
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)

        with open(self.test_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Course ID", "Course Name", "Description"])  # Header
            writer.writerow(["1001", "Course_1", "Description of Course_1"])
            writer.writerow(["1002", "Course_2", "Description of Course_2"])
            writer.writerow(["1003", "Course_3", "Description of Course_3"])

    def tearDown(self):
        """Remove the test file after testing."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_course(self):
        """Test adding a new course."""
        start_time = time.time()
        course_manager = Course(None, None, None, self.test_file)
        course_manager.add_course("1008", "New Course", "This is a new test course")
        elapsed_time = time.time() - start_time

        courses = course_manager.load_courses()
        self.assertTrue(any(c.course_id == "1008" for c in courses))
        print(f"✅ Add Course Test Passed in {elapsed_time:.5f} seconds")

    def test_delete_course(self):
        """Test deleting an existing course."""
        start_time = time.time()
        course_manager = Course(None, None, None, self.test_file)
        course_manager.delete_course("1002")  # Use an existing Course ID from sample data
        elapsed_time = time.time() - start_time

        courses = course_manager.load_courses()
        self.assertFalse(any(c.course_id == "1002" for c in courses))
        print(f"✅ Delete Course Test Passed in {elapsed_time:.5f} seconds")

    def test_modify_course(self):
        """Test modifying an existing course."""
        start_time = time.time()
        course_manager = Course(None, None, None, self.test_file)
        course_manager.modify_course("1003", course_name="Updated Course Name", description="Updated Description")
        elapsed_time = time.time() - start_time

        courses = course_manager.load_courses()
        updated_course = next((c for c in courses if c.course_id == "1003"), None)
        
        self.assertIsNotNone(updated_course)
        self.assertEqual(updated_course.course_name, "Updated Course Name")
        self.assertEqual(updated_course.description, "Updated Description")

        print(f"✅ Modify Course Test Passed in {elapsed_time:.5f} seconds")

if __name__ == "__main__":
    unittest.main()
