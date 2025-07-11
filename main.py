from student import Student
import json
import os

DATA_FILE = "data.json"

# Load data
def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        return [Student.from_dict(d) for d in data]

# Save data
def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump([s.to_dict() for s in students], f, indent=4)

# Add student
def add_student(students):
    roll = input("Roll No: ")
    name = input("Name: ")
    email = input("Email: ")
    course = input("Course: ")
    marks = float(input("Marks: "))
    students.append(Student(roll, name, email, course, marks))
    print("✅ Student added!")

# Display all students
def view_students(students):
    if not students:
        print("No records found.")
        return
    for s in students:
        print(vars(s))

# Search student
def search_student(students):
    keyword = input("Enter name or roll to search: ").lower()
    found = [s for s in students if keyword in s.name.lower() or keyword in s.roll]
    if not found:
        print("❌ No student found.")
    for s in found:
        print(vars(s))

# Update student
def update_student(students):
    roll = input("Enter Roll No to update: ")
    for s in students:
        if s.roll == roll:
            s.name = input(f"Name [{s.name}]: ") or s.name
            s.email = input(f"Email [{s.email}]: ") or s.email
            s.course = input(f"Course [{s.course}]: ") or s.course
            s.marks = float(input(f"Marks [{s.marks}]: ") or s.marks)
            print("✅ Updated.")
            return
    print("❌ Student not found.")

# Delete student
def delete_student(students):
    roll = input("Enter Roll No to delete: ")
    for i, s in enumerate(students):
        if s.roll == roll:
            del students[i]
            print("✅ Deleted.")
            return
    print("❌ Not found.")

# Stats
def show_stats(students):
    print(f"Total Students: {len(students)}")
    if students:
        avg = sum(s.marks for s in students) / len(students)
        print(f"Average Marks: {avg:.2f}")

# Main menu
def main():
    students = load_students()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Stats")
        print("7. Save & Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            show_stats(students)
        elif choice == '7':
            save_students(students)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
