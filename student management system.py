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
def get_name():
   name = input("Enter student's name: ").strip()
   while name == "":
      print("Invalid name")
      name = input("Plz Re-enter student's name: ").strip()
   return name
def get_age():
   while True:
        try:
          age = int(input("Enter student's age: "))
          if age <= 0:
            print("Invalid age")
          else:
             return age
        except ValueError:
          print("please enter a number: ")
def get_marks():
   while True:
        try:
         marks = int(input("Enter student's marks: "))
         if marks < 0 or marks > 100:
           print("Invalid marks")
         else:
            return marks
        except ValueError:
         print("Please Enter a number")
try:
  with open("RECORD.txt","r") as file:
   for line in file:
    try:
      clean_line = line.strip()
      result = clean_line.split(":")
      if len(result) != 4:
         print("Skip this record")
         continue
      s_id = int(result[0])
      age = int(result[2])
      marks = int(result[3])
      if s_id <= 0 or age <= 0 or marks < 0 or marks > 100:
         print("Skip this record")
      elif result[1].strip() == "":
         print("Skip this record")
      else:
         students[s_id] = {'name':result[1].strip(),'age':age,'marks':marks}
    except (ValueError,IndexError):
            print("Skipping invalid record")
except FileNotFoundError:
   print("No saved records found.Starting with an empty list.")
student_id = max(students.keys(),default=0)+1

while True:
   show_menu()
   choice = input("Enter a option number from the Menu above and (6 to exit): ")
   if choice == "1":
    name = get_name()
    age = get_age()
    marks = get_marks()
    students[student_id] = {"name":name, "age":age, "marks":marks}
    print("Student added successfully!")
    student_id +=1
   elif choice == "2":
    if not students:
        print("No student registered yet!")
    else:
      for s_id,info in students.items():
         print(f"Student ID: {s_id}")
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
        new_name = get_name()
        new_age = get_age()
        new_marks = get_marks()
        students[change]['name'] = new_name
        students[change]['age'] = new_age
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
        if len(students) == 0:
          print("No student registered anymore")
    else:
        print("Student not found")
   elif choice == "6":
    print("Thank u for using \"THE BEST STUDENT MANAGEMENT SYSTEM\"")
    break
   else:
      print("Invalid input!plz try again.")
with open("RECORD.txt","w") as file:
  for s_id,info in students.items():
   file.write(f"{str(s_id)}:{info['name']}:{info['age']}:{info['marks']}\n")
