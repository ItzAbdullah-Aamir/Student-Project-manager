print("-------------STUDENT MANAGER SYSTEM-----------------")
print("--MAIN MENU--")
print("1.Add Student")
print("2.View Student")
print("3.Search Student")
print("4.Update Student")
print("5.Delete Student")
print("6.exit")
students = {}
student_id = 1
choice = input("Enter a option number from the Menu above: ")
if choice == "1":
    name = input("Enter student name: ")
    age = input("Enter student's age: ")
    marks = input("Enter student's marks: ")
    students[student_id] = {"name":name, "age":age, "marks":marks}
    student_id +=1
if choice == "2":
    for id,info in students.items():
        print(f"""Student ID: {id}\n
              Name: {info['name']}\n
              Age: {info['age']}\n
              Marks: {info['marks']}""")
if choice == "3":
    print()