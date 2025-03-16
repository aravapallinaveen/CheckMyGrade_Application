from login import LoginUser
from student import Student
from course import Course
from professor import Professor
from grades import Grades
from student import StudentManager

def main():
    logged_in = False
    user_role = None
    email = None
    login_user = LoginUser()  # Create an instance of LoginUser
    grades = Grades()  # Create an instance of Grades

    while True:
        if not logged_in:
            print("\n🏫 **CheckMyGrade - Main Menu**")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                email = input("Enter email: ")
                password = input("Enter password: ")
                role = input("Enter role (student/professor): ").strip().lower()
                if role not in ["student", "professor"]:
                    print("❌ Invalid role! Choose from student, professor")
                    continue
                login_user.register(email, password, role)

            elif choice == "2":
                email = input("Enter email: ")
                password = input("Enter password: ")
                role = login_user.login(email, password)
                if role:
                    logged_in = True
                    user_role = role
                    print(f"✅ Welcome, {email}! You are logged in as {role.capitalize()}.")

            elif choice == "3":
                print("👋 Exiting application. Goodbye!")
                break

            else:
                print("❌ Invalid choice! Please enter a valid option.")

        else:
            if user_role == "admin":
                logged_in = admin_menu(email, login_user)
            elif user_role == "professor":
                logged_in = professor_menu(email, login_user)
            elif user_role == "student":
                logged_in = student_menu(email, login_user)

def admin_menu(email, login_user):
    while True:
        print("\n🏫 **Admin Menu**")
        print("1. Change Password")
        print("2. Logout")
        print("3. Manage Students")
        print("4. Manage Courses")
        print("5. Manage Professors")
        print("6. Grade Report")

        choice = input("Enter choice: ")

        if choice == "1":
            old_password = input("Enter current password: ")
            new_password = input("Enter new password: ")
            if login_user.change_password(email, old_password, new_password):
                print("🔒 Password updated successfully!")

        elif choice == "2":
            login_user.logout()
            return False

        elif choice == "3":
            manage_students()

        elif choice == "4":
            manage_courses()

        elif choice == "5":
            manage_professors()

        elif choice == "6":
            grades = Grades()  # Create an instance of Grades
            grades.display_grade_report()  # Call the method on the instance

        else:
            print("❌ Invalid choice! Please enter a valid option.")

def professor_menu(email, login_user):
    while True:
        print("\n🏫 **Professor Menu**")
        print("1. Change Password")
        print("2. Logout")
        print("3. Manage Students")
        print("4. Manage Courses")
        print("5. Grade Report")

        choice = input("Enter choice: ")

        if choice == "1":
            old_password = input("Enter current password: ")
            new_password = input("Enter new password: ")
            if login_user.change_password(email, old_password, new_password):
                print("🔒 Password updated successfully!")

        elif choice == "2":
            login_user.logout()
            return False

        elif choice == "3":
            manage_students()

        elif choice == "4":
            manage_courses()

        elif choice == "5":
            grades = Grades()  # Create an instance of Grades
            grades.display_grade_report()  # Call the method on the instance

        else:
            print("❌ Invalid choice! Please enter a valid option.")

def student_menu(email, login_user):
    # Change the path to use the data directory
    student_manager = StudentManager('data\\students.csv')
    while True:
        print("\n🏫 **Student Menu**")
        print("1. Change Password")
        print("2. Logout")
        print("3. Check My Grades")
        print("4. Check My Marks")

        choice = input("Enter choice: ")

        if choice == "1":
            old_password = input("Enter current password: ")
            new_password = input("Enter new password: ")
            if login_user.change_password(email, old_password, new_password):
                print("🔒 Password updated successfully!")

        elif choice == "2":
            login_user.logout()
            return False

        elif choice == "3":
            grades = student_manager.check_my_grades(email)
            if grades:
                print("Your grades:")
                for grade in grades:
                    print(grade)
            else:
                print("❌ Student not found with this email.")

        elif choice == "4":
            marks = student_manager.check_my_marks(email)
            if marks:
                print("Your marks:")
                for mark in marks:
                    print(mark)
            else:
                print("❌ Student not found with this email.")

        else:
            print("❌ Invalid choice! Please enter a valid option.")

def manage_students():
    student_manager = StudentManager('data\\students.csv')  # Adjust the path to your student file
    while True:
        print("\n📚 Student Management")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Modify Student")
        print("4. View Students")
        print("5. Check Student Grades")
        print("6. Check Student Marks")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            email = input("Enter Student Email: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            course_id = input("Enter Course ID: ")
            marks = input("Enter Marks: ")  # Grade auto-calculated

            student_manager.add_student(email, first_name, last_name, course_id, marks)

        elif choice == "2":
            email = input("Enter Student Email to Delete: ")
            course_id = input("Enter Course ID to Delete: ")  # Ask for course ID
            student_manager.delete_student(email, course_id)

        elif choice == "3":
            email = input("Enter Student Email to Modify: ")
            course_id = input("Enter Course ID to Modify: ")  # Ask for course ID

            first_name = input("Enter New First Name (leave blank to keep same): ")
            last_name = input("Enter New Last Name (leave blank to keep same): ")
            marks = input("Enter New Marks (leave blank to keep same): ")

            student_manager.modify_student(email, course_id,
                                           first_name or None, 
                                           last_name or None, 
                                           marks or None)

        elif choice == "4":
            student_manager.display_students()

        elif choice == "5":
            email = input("Enter Student Email to Check Grade: ")
            grades = student_manager.check_my_grades(email)
            if grades:
                print("Your grades:")
                for grade in grades:
                    print(grade)
            else:
                print("❌ Student not found with this email.")

        elif choice == "6":
            email = input("Enter Student Email to Check Marks: ")
            marks = student_manager.check_my_marks(email)
            if marks:
                print("Your marks:")
                for mark in marks:
                    print(mark)
            else:
                print("❌ Student not found with this email.")

        elif choice == "7":
            break

        else:
            print("❌ Invalid choice! Please enter a valid option.")

def manage_courses():
    grades = Grades()  # Create an instance of Grades
    while True:
        print("\nCourse Management")
        print("1. Add Course")
        print("2. Delete Course")
        print("3. Modify Course")
        print("4. View Courses")
        print("5. View Average Score")
        print("6. View Median Score")
        print("7. Generate Course Report")
        print("8. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            course_id = input("Enter Course ID: ")
            course_name = input("Enter Course Name: ")
            description = input("Enter Course Description: ")

            course = Course(course_id, course_name, description)
            course.add_course(course_id, course_name, description)

        elif choice == "2":
            course_id = input("Enter Course ID to Delete: ")
            course = Course(course_id, None, None)
            course.delete_course(course_id)

        elif choice == "3":
            course_id = input("Enter Course ID to Modify: ")
            course_name = input("Enter New Course Name (leave blank to keep same): ") or None
            description = input("Enter New Description (leave blank to keep same): ") or None

            course = Course(course_id, course_name, description)
            course.modify_course(course_id, course_name, description)

        elif choice == "4":
            course = Course(None, None, None)
            course.display_courses()

        elif choice == "5":
            course_id = input("Enter Course ID: ")
            avg_score = grades.average_score(course_id)
            if avg_score is not None:
                print(f"Average score for course {course_id}: {avg_score}")
            else:
                print("No scores found for this course.")

        elif choice == "6":
            course_id = input("Enter Course ID: ")
            med_score = grades.median_score(course_id)
            if med_score is not None:
                print(f"Median score for course {course_id}: {med_score}")
            else:
                print("No scores found for this course.")

        elif choice == "7":
            course_id = input("Enter Course ID: ")
            report = grades.generate_report('Course ID', course_id)
            if report:
                print(f"Report for course {course_id}:")
                for entry in report:
                    print(entry)
            else:
                print("No data found for this course.")

        elif choice == "8":
            break

        else:
            print("Invalid choice! Please enter a valid option.")

def manage_professors():
    professor_manager = Professor()  # Create an instance of Professor
    grades = Grades()  # Create an instance of Grades
    while True:
        print("\n📚 Professor Management")
        print("1. Add Professor")
        print("2. Delete Professor")
        print("3. Modify Professor")
        print("4. View Professors")
        print("5. Show Course Details by Professor")
        print("6. Generate Professor Report")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            professor_id = input("Enter Professor ID: ")
            name = input("Enter Name: ")
            rank = input("Enter Rank: ")
            course_id = input("Enter Course ID: ")
            professor_manager.add_professor(professor_id, name, rank, course_id)

        elif choice == "2":
            professor_id = input("Enter Professor ID to Delete: ")
            professor_manager.delete_professor(professor_id)

        elif choice == "3":
            professor_id = input("Enter Professor ID to Modify: ")
            name = input("Enter New Name (leave blank to keep same): ")
            rank = input("Enter New Rank (leave blank to keep same): ")
            course_id = input("Enter New Course ID (leave blank to keep same): ")

            professor_manager.modify_professor(professor_id, 
                                               name or None, 
                                               rank or None, 
                                               course_id or None)

        elif choice == "4":
            professor_manager.display_professors()  # Call the method on the instance

        elif choice == "5":
            professor_id = input("Enter Professor ID to View Course Details: ")
            professor_manager.show_course_details_by_professor(professor_id)

        elif choice == "6":
            professor_id = input("Enter Professor ID: ")
            report = grades.generate_professor_report(professor_id)

            if "error" in report:
                print("❌ No data found for this professor.")
            elif report["Students"]:
                print(f"\n📊 Report for Professor {professor_id} ({report['Name']}):")
                print(f"📚 Course ID: {report['Course ID']}")
                print(f"{'Email':<30} {'Marks':<10} {'Grade':<10}")
                print("-" * 50)
                for entry in report["Students"]:
                    print(f"{entry['Student Email']:<30} {entry['Marks']:<10} {entry['Grade']:<10}")
            else:
                print(f"📊 Professor {report['Name']} has no students enrolled in Course ID: {report['Course ID']}.")


        elif choice == "7":
            break

        else:
            print("❌ Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
