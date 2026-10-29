students = []
n = int(input("Enter the number of students:"))
for i in range(n):
    print(f"\nEnter details of Student {i + 1}:")

    name = input("Enter student name:")
    usn = input("Enter USN:")

    mark1 = float(input("Enter marks 1:"))
    mark2 = float(input("Enter marks 2:"))
    mark3 = float(input("Enter marks 3:"))

    total = mark1 + mark2 + mark3
    average = total / 3

    # Store student details in a list
    students.append([name, usn, mark1, mark2,mark3, total, average])

# Display table after accepting all inputs
print("\n"+"="*94)
print("           STUDENT MARKS REPORT")
print("=" * 94)

print(f"{'Name':<15} {'USN':<15} {'course1':>10} {'cource2':<10} {'course3':<18} {'total':<10} {'average':<10}")
print("-"*94)
for students in students:
    name,usn,m1,m2,m3,total,avg=students
    print(f"{name:<15} {usn:<15} {m1:<10.2f} {m2:<10.2f} {m3:<10.2f} {total:<10.2f} {average:<10.2f}")
print("="*94)