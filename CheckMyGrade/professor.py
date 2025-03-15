import csv
import os

class Professor:
    PROFESSOR_FILE = "data/professors.csv"

    def __init__(self, professor_id=None, name=None, rank=None, course_id=None):
        self.professor_id = professor_id
        self.name = name
        self.rank = rank
        self.course_id = course_id

    def load_professors(self):
        professors = []
        if os.path.exists(self.PROFESSOR_FILE):
            with open(self.PROFESSOR_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    if len(row) == 4:  # Ensure correct column count
                        professors.append(Professor(*row))
                    else:
                        print(f"⚠ Skipping invalid row: {row}")
        return professors

    def save_professors(self, professors):
        with open(self.PROFESSOR_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Professor ID", "Name", "Rank", "Course ID"])
            for professor in professors:
                writer.writerow([professor.professor_id, professor.name, professor.rank, professor.course_id])

    def add_professor(self, professor_id, name, rank, course_id):
        professors = self.load_professors()
        professors.append(Professor(professor_id, name, rank, course_id))
        self.save_professors(professors)
        print("✅ Professor added successfully!")

    def delete_professor(self, professor_id):
        professors = self.load_professors()
        updated_professors = [p for p in professors if p.professor_id != professor_id]
        
        if len(updated_professors) == len(professors):
            print("⚠ Professor not found!")
        else:
            self.save_professors(updated_professors)
            print("✅ Professor deleted successfully!")

    def modify_professor(self, professor_id, name=None, rank=None, course_id=None):
        professors = self.load_professors()
        found = False

        for professor in professors:
            if professor.professor_id == professor_id:
                found = True
                professor.name = name or professor.name
                professor.rank = rank or professor.rank
                professor.course_id = course_id or professor.course_id
                break

        if not found:
            print("⚠ Professor not found!")
            return

        self.save_professors(professors)
        print("✅ Professor record updated successfully!")

    def display_professors(self):
        professors = self.load_professors()
        if not professors:
            print("⚠ No professors available!")
            return

        print("\nProfessor List:")
        print("------------------------------------------------------------")
        print(f"{'ID':<25}{'Name':<20}{'Rank':<15}{'Course ID'}")
        print("------------------------------------------------------------")
        for professor in professors:
            print(f"{professor.professor_id:<25}{professor.name:<20}{professor.rank:<15}{professor.course_id}")
        print("------------------------------------------------------------")

    def show_course_details_by_professor(self, professor_id):
        professors = self.load_professors()
        professor = next((p for p in professors if p.professor_id == professor_id), None)

        if not professor:
            print(f"⚠ No professor found with ID {professor_id}")
            return

        print(f"\n📌 Professor {professor.name} (ID: {professor.professor_id}) is teaching Course ID: {professor.course_id}")
