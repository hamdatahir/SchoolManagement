# Improved Python version

class Student:
    def __init__(self, sid, name, marks):
        self.id = sid
        self.name = name
        self.marks = marks

    def display(self):
        print("\n--- Student Record ---")
        print(f"ID    : {self.id}")
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")

        if self.marks >= 50:
            print("Status: Pass")
        else:
            print("Status: Fail")

# Main program with menu
students = []

while True:
    print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\n--- Add New Student ---")
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        # Validation
        if marks < 0 or marks > 100:
            print("Error: Marks should be between 0 and 100")
        else:
            s = Student(sid, name, marks)
            students.append(s)
            print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for s in students:
                s.display()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
