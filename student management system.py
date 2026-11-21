def show_menu(): 
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
while True:
   show_menu()
   choice = input("Enter a option number from the Menu above and (6 to exit): ")
   if choice == "1":
    name = input("Enter student name: ")
    age = input("Enter student's age: ")
    marks = input("Enter student's marks: ")
    students[student_id] = {"name":name, "age":age, "marks":marks}
    student_id +=1
   elif choice == "2":
    for id,info in students.items():
        print(f"""Student ID: {id}\n
              Name: {info['name']}\n
              Age: {info['age']}\n
              Marks: {info['marks']}""")
   elif choice == "3":
    search = int(input("Enter the Id you searching for: "))
    if search in students:
        print(f"Student Name: {students[search]['name']}")
        print(f"Student Age: {students[search]['age']}")
        print(f"Student marks: {students[search]['marks']}")
    else:
        print("Student not found")
   elif choice == "4":
    change = int(input("Enter the id you want to change: "))
    if change in students:
        new_name = input("Enter your new name: ")
        students[change]['name'] = new_name
        new_age = int(input("Enter your new age: "))
        students[change]['age'] = new_age
        new_marks = int(input("Enter your new marks: "))
        students[change]['marks'] = new_marks
        print("Student updated successfully!")
    else:
        print("Student id does not exist")
   elif choice == "5":
    delete = int(input("Enter the student id to delete: "))
    if delete in students:
        del students[delete]
        print("Student deleted successfully!")
    else:
        print("Student not found")
   elif choice == "6":
    print("Thank u for using \"THE BEST STUDENT MANAGEMENT SYSTEM\"")
    break
   else:
      print("Invalid input!plz try again.")