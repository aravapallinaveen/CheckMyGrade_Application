import csv

COURSE_FILE = "data/courses.csv"

def generate_courses():
    """Generate 4 course records and save to a CSV file."""
    courses = [
        {"course_id": 101, "course_name": "Mathematics", "description": "Introduction to Mathematics"},
        {"course_id": 102, "course_name": "Physics", "description": "Fundamentals of Physics"},
        {"course_id": 103, "course_name": "Chemistry", "description": "Basics of Chemistry"},
        {"course_id": 104, "course_name": "Biology", "description": "Principles of Biology"}
    ]

    with open(COURSE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Course ID", "Course Name", "Description"])  # Header
        
        for course in courses:
            writer.writerow([course["course_id"], course["course_name"], course["description"]])

    print(f"✅ 4 course records generated in '{COURSE_FILE}'.")

generate_courses()