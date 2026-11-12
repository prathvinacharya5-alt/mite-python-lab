def display_list(items):
    print("List contents    :",items)
    
def display_tuple(items):
    print("tuple contents:",items)
    
#A.List operations
n=int(input("How many integers?"))
numbers=[int(input(f"Enter element{i+1}:"))for i in range(n)]

value=int(input("Enter value to insert:"))
position=int(input("Enter position(0-based):"))
if 0<=position<=len(numbers):
    numbers.insert(position,value)
else:
    print("Invalid position")
    
value=int(input("Enter element to delet:"))
if value in numbers:
    numbers.remove(value)
else:
    print("Element not found")
    
numbers.sort()
print("Sorted list :",numbers)
numbers.reverse()
print("Reversed list:",numbers)

#B.Tuple operations
names=tuple(input("Enter student names separated by space:").split())
print("Tuple:",names)
search_name=input("Enter name to count:")
print("Count:",names.count(search_name))
index_name=input("Enter name to find index:")
if index_name in names:
    print("Index:",names.index(index_name))
else:
    print("Name not found")
    
#C.Dictionary operations
students={"4MT26CS001":"Ananya","4MT26CS002":"Rahul"}
new_usn=input("Enter new USN:")
new_name=input("Enter new student name:")
students[new_usn]=new_name
update_usn=input("Enter USN to update:")
if update_usn in students:
    students[update_usn]=input("Enter updated name:")
else:
    print("USN not found")
delet_usn=input("Enter USN to delete:")
if delete_usn in students:
    del students[delete_usn]
else:
    print("USN not found")
    
print("Keys:",list(students.keys()))
print("Values:",list(students.values()))

#D.pass collections to functions
display_list(numbers)
display_tuple(names)
display_disctionary(students)
