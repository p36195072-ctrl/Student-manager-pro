import json
try:
    with open("students.json", "r") as file:
        students = json.load(file)
        print(students)
        
except FileNotFoundError:
    students = {}


while True:

    print("\n===== STUDENT MANAGER =====\n")
    print("1. Add Student")
    print("2. Search Student")
    print("3. View All Students")
    print("4. Delete Student")
    print("5. Edit Students")

    print("6. Exit")
    print("Total students:", len(students))

    choice = input("Enter choice: ")

    def save_data():
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

    def add_student():

        try:
            name = input("Enter name: ").strip()
            if name == "":
                print("Name can't be empty")
                return

            age = input("Enter age: ").strip()
            if age == "":
                print("Age can't be empty")
                return

            city = input("Enter city: ").strip()
            if city == "":
                print("City can't be empty")
                return

            student_class = input("Enter class: ").strip()
            if student_class == "":
                print("Student class can't be empty")
                return

            student_class = int(student_class)

            students[name] = {
                "age": age,
                "city": city,
                "class": student_class
            }

            save_data()
            print("Student Added!")
        except ValueError:
            print("Class must be a number")
        return
    
    

    def search_student():

        
        name = input("Search student: ").strip()

        if name == "":
            print("Name in search can't be empty.")
            return

        if name in students:
            print(students[name])
        else:
            print("Student Not Found")
        
    

        
        
    def view_all_student():

        
        if len(students) == 0:
            print("No students found")
        
        else:
            for name, details in students.items():
                print(name, ":", details)
    
    def deletestudent():

        
        name = input("Enter student name: ").strip()
        if name == "":
            print ("You have to enter name to delete")
            return

        if name in students:
            del students[name]
            print("Deleted Successfully")
        else:
            print("Student Not Found")

        save_data()


    
    def edit_task():
        print(students)
        name  = input("Enter the name to edit:")
        if name in students:
            age = input("Enter new age:")
            city = input("Enter new city:")

            students[name]["age"] = age
            students[name]["city"] = city
            
            save_data()

            print("Student updated")
        else:
            print("student not found")
            save_data()

   
    def Exit():

    
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Data saved successfully!")
        print("Exiting...")
        
    if choice == "1":
         add_student()
    
    if choice == "2":
        search_student()
    
    if choice == "3":
        view_all_student()

    if choice == "4":
        deletestudent()
    
    if choice == "5":
        edit_task()
    
    if choice == "6":
        Exit()
        break