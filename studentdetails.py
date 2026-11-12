students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")
    
    student = {"Name": name, "Roll No": roll_no, "Marks": marks}
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    
    print("\n--- Student Details ---")
    for s in students:
        print(f"Name: {s['Name']} | Roll No: {s['Roll No']} | Marks: {s['Marks']}")
    print()

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
