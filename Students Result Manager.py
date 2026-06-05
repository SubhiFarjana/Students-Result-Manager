student = {}

while True:
    print("-----STUDENT MANAGER APP-----")
    print(" Click 1 to add student")
    print(" Click 2 to view student")
    print(" Click 3 to check result ")
    print(" Click 4 to exit")

    choice=int(input("enter your choice: "))

    if choice == 1:
        name=input("Enter students name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} Successfully added! ")

    elif choice == 2:
        if not student: 
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    elif choice == 3:
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks <= 100 and marks >= 90:
                print("Grade A")
            elif marks >= 80:
                print("Grade A-")
            elif marks >= 70:
                print("Grade B")
            elif marks >= 60:
                print("Grade B-")
            elif marks >= 50:
                print("Grade C")
            elif marks >= 40:
                print("Grade D")
            elif marks < 40:
                print("Fail")
            else:
                print("in-valid input")
        else:
            print("Student not found")
    elif choice == 4:
        print("Exiting....")  
        break
    else:
        print("In-valid input")    
