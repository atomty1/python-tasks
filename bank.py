import random
accounts = []
def bank():
    print(accounts)
    print("Welcome to our bank")
    main_menu = input("1. Register  2. Login: ")
    if(main_menu== "1"):
        register()
    elif(main_menu == "2"):
        login()

def register():
    email = input("Enter your email: ") #kenny@gmail.com
    seen = False
    for account in accounts:
        if(account["email"] == email):
            seen = True
            break
    if(seen):
        print("email already exist")
    else:
        firstname = input("Enter your firstname: ")
        lastname = input("Enter your lastname: ")
        password = input("Enter your password: ")
        account_num = random.randrange(3000000000, 3999999999)
        new_account = {"firstname": firstname, "lastname": lastname, 
                       "email": email, "password": password, "account_no": account_num, "balance": 50000}
        accounts.append(new_account)
        print(f"Registration successful, this is your new account number: {account_num}")
    bank()
        
def login():
    email_or_account_num = input("Enter your email or account number: ")
    password = input("Enter your password: ")
    logged_in_user = None
    for account in accounts:
        if(account["password"] == password and 
           (account["email"] == email_or_account_num or account["account_no"] == email_or_account_num)):
            logged_in_user = account #  {"firstname": "Taye", "balance": 50000}
            break
    if(logged_in_user is None):
        print("Incorrect logged in details")
    else:
        print("login successful")
        transfer(logged_in_user) 
        
def transfer(user):
    amount = float(input("Enter the amount you want to transfer: "))
    account_number_or_email = input("Enter the account number or email of the recipient: ")
    recipient = None
    for account in accounts:
        if(account["email"] == account_number_or_email or account["account_no"] == account_number_or_email):
            recipient = account
            break
    if(user["balance"] < amount):
        print("Insufficient funds")
    elif(recipient is None):
        print("User not found")
    else:
        user["balance"] = user["balance"] - amount
        recipient["balance"]  = recipient["balance"] + amount
        print(f"You have successfully transferred {amount} to {account_number_or_email}.")

    user_choice = input("1. Transfer 2. Main menu")
    if(user_choice == "1"):
        transfer(user)
    elif(user_choice == "2"):
        bank()







bank()
