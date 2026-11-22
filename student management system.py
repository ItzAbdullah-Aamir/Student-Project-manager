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
def show_student(student):
   print(f"Name  : {student['name']}")
   print(f"Age   : {student['age']}")
   print(f"Marks : {student['marks']}")
while True:
   show_menu()
   choice = input("Enter a option number from the Menu above and (6 to exit): ")
   if choice == "1":
    name = input("Enter student name: ")
    while name == "":
       print("Invalid name")
       name = input("plz reenter ur name: ")
    while True:
     try:
       age = int(input("Enter student's age: "))
       if age < 0:
        print("Invalid age")
       else:
          break
     except ValueError:
       print("please enter a number: ")
    while True:
     try:
      marks = int(input("Enter student's marks: "))
      if marks < 0 or marks > 100:
        print("Invalid marks")
      else:
         break
     except ValueError:
      print("Please Enter a number")
    students[student_id] = {"name":name, "age":age, "marks":marks}
    print("Student added successfully!")
    student_id +=1
   elif choice == "2":
    if students == {}:
        print("No student registered yet!")
    else:
      for id,info in students.items():
         print(f"Student ID: {id}")
         show_student(info)
   elif choice == "3":
    while True:
       try:
        search = int(input("Enter the Id you searching for: "))
        break
       except ValueError:
          print("Plz enter a number")
    if search in students:
        show_student(students[search])
        print("Student Found successfully!")
    else:
        print("Student not found")
   elif choice == "4":
    while True:
        try:
          change = int(input("Enter the Id you want to update: "))
          break
        except ValueError:
          print("PLz enter a number")
    if change in students:
        new_name = input("Enter your new name: ")
        while new_name == "":
               print("Invalid name")
               new_name = input("plz reenter ur name: ")
        students[change]['name'] = new_name
        while True:
             try:
               new_age = int(input("Enter student's new age: "))
               if new_age < 0:
                print("Invalid age")
               else:
                  break
             except ValueError:
               print("please enter a number: ")
        students[change]['age'] = new_age
        while True:
             try:
              new_marks = int(input("Enter student's marks: "))
              if new_marks < 0 or new_marks > 100:
                print("Invalid marks")
              else:
                 break
             except ValueError:
              print("Please Enter a number")
        students[change]['marks'] = new_marks
        print("Student updated successfully!")
    else:
        print("Student id does not exist")
   elif choice == "5":
    while True:
            try:
              delete = int(input("Enter the Id you want to delete: "))
              break
            except ValueError:
              print("PLz enter a number")
    if delete in students:
        del students[delete]
        print(f"Student id {delete} deleted successfully!")
        print(f"Number of student registered: {len(students)}")
        if len(students) == {}:
          print("No student registered anymore")
    else:
        print("Student not found")
   elif choice == "6":
    print("Thank u for using \"THE BEST STUDENT MANAGEMENT SYSTEM\"")
    break
   else:
      print("Invalid input!plz try again.")