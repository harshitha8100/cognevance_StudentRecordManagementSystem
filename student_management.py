import os

FILE_NAME = "students.txt"


def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    students.append(data)
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(",".join(student) + "\n")


def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Class/Course: ")

    try:
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Invalid Marks!")
        return

    students.append([student_id, name, course, str(marks)])
    save_students(students)

    print("Student Added Successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No Records Found!")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"ID: {student[0]}, Name: {student[1]}, "
            f"Course: {student[2]}, Marks: {student[3]}"
        )


def search_student():
    students = load_students()

    student_id = input("Enter Student ID to Search: ")

    for student in students:
        if student[0] == student_id:
            print("\nStudent Found:")
            print(
                f"ID: {student[0]}, Name: {student[1]}, "
                f"Course: {student[2]}, Marks: {student[3]}"
            )
            return

    print("Student Not Found!")


def update_student():
    students = load_students()

    student_id = input("Enter Student ID to Update: ")

    for student in students:
        if student[0] == student_id:
            student[1] = input("Enter New Name: ")
            student[2] = input("Enter New Course: ")

            try:
                student[3] = str(float(input("Enter New Marks: ")))
            except ValueError:
                print("Invalid Marks!")
                return

            save_students(students)
            print("Record Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to Delete: ")

    updated_students = [s for s in students if s[0] != student_id]

    if len(updated_students) == len(students):
        print("Student Not Found!")
    else:
        save_students(updated_students)
        print("Record Deleted Successfully!")


def performance_report():
    students = load_students()

    if not students:
        print("No Records Found!")
        return

    print("\n--- Student Performance Report ---")

    for student in students:
        marks = float(student[3])

        if marks >= 90:
            grade = "A+"
        elif marks >= 75:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print(
            f"ID: {student[0]}, Name: {student[1]}, "
            f"Marks: {marks}, Grade: {grade}"
        )


def main():
    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Student Performance Report")
        print("7. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            performance_report()
        elif choice == "7":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Try Again.")


if __name__ == "__main__":
    main()