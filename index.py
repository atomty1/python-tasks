def get_maximum():
    first_num = float(input("Enter the first number: ")) # 7
    second_num = float(input("Enter the second number: ")) # 10
    third_num = float(input("Enter the third number: "))  #10
    fourth_num = float(input("Enter the fourth number: ")) # 8
    greatest_num = max(first_num, second_num, third_num, fourth_num)
    print(f"The greatest number is {greatest_num}")
    print("Do you want to go again?")
    rerun = input("1. Yes 2. No: ")
    if(rerun == "1"):
        get_maximum()
    else:
        print("Thanks for using this. Bye!!!")
    

get_maximum()

# functions, if statement, loop, variable
        
