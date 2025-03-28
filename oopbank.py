import random

class Bank:
    def main_menu(self):
        print("Welcome to our bank")
        main_menu_choice = input("1. Register  2. Login: ")
        if main_menu_choice == "1":
            account = Account("", "", "", "") 
            account.register()
        elif main_menu_choice == "2":
            account = Account("", "", "", "") 
            account.login()


class Account:
    accounts = []

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.account_no = random.randrange(3000000000, 3999999999)
        self.balance = 50000
        self.accounts.append(self)  
    
    def check_email_exist(self, email_or_acc_no):
        for account in self.accounts:
            if account.email == email_or_acc_no or account.account_no == email_or_acc_no:
                return account
        return None

    def register(self):
        print("Success")
        email = input("Enter your email: ")  # Example: kenny@gmail.com
        check_email = self.check_email_exist(email)
        if check_email:
            print("Email already exists")
        else:
            firstname = input("Enter your firstname: ")
            lastname = input("Enter your lastname: ")
            password = input("Enter your password: ")
            Account(firstname, lastname, email, password)  
            Bank().main_menu()
  
    def login(self):
        email_or_account_num = input("Enter your email or account number: ")
        password = input("Enter your password: ")
        check_account = self.check_email_exist(email_or_account_num)
        if check_account and check_account.password == password:
            print("Login Successful")
            self.transfer()
        else:
            print("Incorrect login details")
    
    def transfer(self):
        amount = float(input("Enter the amount you want to transfer: "))
        account_number_or_email = input("Enter the account number or email of the recipient: ")
        recipient = self.check_email_exist(account_number_or_email)
        if recipient is None:
            print("Recipient does not exist")
        elif self.balance < amount:
            print("Out of balance")
        else:
            self.balance -= amount
            recipient.balance += amount
            print("Transfer Successful")
            self.show_balance()
    
    def show_balance(self):
        print(f"Your balance is {self.balance}")


new_bank = Bank()
new_bank.main_menu()
