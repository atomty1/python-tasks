def calculator():
    print("Welcome to Taye's calculator")
    user_operation = input("1. + 2. - 3. * 4. / : ")
    if(user_operation== "1"):
        addition()
    elif(user_operation == "2"):
        subtraction()
    elif(user_operation == "3"):
        multiplication()
    elif(user_operation == "4"):
        division()
        
    print("Do you want to perform another arithmetic? ")
    perform_another = input("1. Yes 2. No : ")
    if(perform_another == "1"):
        calculator()
    else:
        print("Thanks for using the calculator. Bye!!!")
        
        

def addition():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num + second_num
    print(f"The addition of {first_num} and {second_num} is {result}")

def subtraction():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num - second_num
    print(f"The subtraction of {first_num} and {second_num} is {result}")

def multiplication():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num * second_num
    print(f"The multiplication of {first_num} and {second_num} is {result}")

def division():
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    result = first_num / second_num
    print(f"The division of {first_num} and {second_num} is {result}")