all_students = []

def school():
    print("Welcome")
    print("What do you want to do?")
    sign_in_choice = input("1. Register 2. Login: ")
    if (sign_in_choice == "1"):
        register()
    elif(sign_in_choice == "2"):
        login()
    else:
        print("Incorrect entry")
        school()



def register():
    firstname = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    student_exist = False
    for student in all_students:
        if(student["email"] == email):
            print("Email already exist")
            student_exist = True
            break
    if(student_exist):
        school()
    else:
        new_student = {"firstname": firstname, "lastname": lastname, "email": email, "pass": password}
        all_students.append(new_student)
        print("registration successful")
        print(all_students)
        school()

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    found_student = None
    for student in all_students:
        if(student["email"] == email and student["pass"] == password):
            found_student = student
            break
    if found_student is None:
        print("Incorrect login details")
        school()
    else:
        print(f"{found_student["firstname"]} {found_student["lastname"]} has logged in successfully")
        school()


            

school()