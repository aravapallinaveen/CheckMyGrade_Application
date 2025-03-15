import unittest
import csv
import os
import sys

# Adjust the sys.path to include the directory containing the professor module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "CheckMyGrade")))

from professor import Professor

class TestProfessorManagement(unittest.TestCase):
    """Unit tests for the Professor class."""

    def setUp(self):
        """Set up test data with a few professor records and ensure the test file is used for each test case."""
        self.test_file = "data/test_professors.csv"  # Use a temporary test file
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)

        with open(self.test_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Professor ID", "Name", "Rank", "Course ID"])  # Header
            writer.writerow(["prof1@university.com", "Professor_1", "Doctorate", "1001"])
            writer.writerow(["prof2@university.com", "Professor_2", "Master's", "1002"])
            writer.writerow(["prof3@university.com", "Professor_3", "Doctorate", "1003"])

        self.professor_manager = Professor(None, None, None, None)
        self.original_file = Professor.PROFESSOR_FILE
        Professor.PROFESSOR_FILE = self.test_file  # Override global file path

    def tearDown(self):
        """Remove the test file and restore the original file path."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        Professor.PROFESSOR_FILE = self.original_file

    def test_add_professor(self):
        """Test adding a new professor."""
        self.professor_manager.add_professor("newprof@university.com", "Dr. New", "PhD", "1050")

        with open(self.test_file, "r") as file:
            lines = list(csv.reader(file))

        self.assertIn(["newprof@university.com", "Dr. New", "PhD", "1050"], lines)
        print("✅ Add Professor Test Passed")

    def test_delete_professor(self):
        """Test deleting an existing professor."""
        self.professor_manager.delete_professor("prof2@university.com")

        with open(self.test_file, "r") as file:
            lines = list(csv.reader(file))

        professor_ids = [line[0] for line in lines[1:]]  # Skip header
        self.assertNotIn("prof2@university.com", professor_ids)
        print("✅ Delete Professor Test Passed")

    def test_modify_professor(self):
        """Test modifying an existing professor."""
        self.professor_manager.modify_professor("prof3@university.com", name="Updated Professor_3")

        with open(self.test_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "prof3@university.com":
                    self.assertEqual(row[1], "Updated Professor_3")

        print("✅ Modify Professor Test Passed")

if __name__ == "__main__":
    unittest.main()
