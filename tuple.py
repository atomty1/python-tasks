import random
accounts = []
def bank_app():
    print("Welcome to my bank")
    main_menu = input("1. Register 2. Login")
    if(main_menu == "1"):
        register()
    elif(main_menu == "2"):
        login()
    


def register():
    firstname = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
   
    
    email_exists = None
    for account in accounts:
        if(account["email"] == email):
            email_exists = True
            break
    if(email_exists is True):
        print("email already exist")
    else:
        account_number = random.randint(1000000000, 9999999999)
        new_user = {"firstname": firstname, "lastname": lastname, 
                "email": email, "password": password, "account": account_number}
        accounts.append(new_user)
        print(f"Registration successful. Here is your account number: {account_number}")

def login():
    email_or_acc_num = input("Enter your email or account number: ")
    password = input("Enter your pasword: ")
    found_user = None
    for account in accounts:
        if(
            password == account["password"] and 
           (email_or_acc_num == account["email"] or email_or_acc_num == account["account"]) 
           ):
            found_user = account
            print("login successful")
            break
    if(found_user is None):
        print("Incorrect login details")
        bank_app()
    else:
        print(f"Your fullname is {found_user["firstname"]} {found_user["lastname"]}")
        bank_app()
        

# accounts = [
#                 {"firstname": "Taye", "lastname": "Abidakun", "password": "12345", "account": "0986", "email": "taye@gmail.com"},
#                 {"firstname": "Kenny", "lastname": "Ojo", "password": "98765", "account": "1268", "email": "kenny@gmail.com"}

#             ]
