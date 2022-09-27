"""2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""


while True:
    print('+'*40)
    inpt = int(input("press 1 for addition\npress 2 for substraction\npress 3 for multiplication\npress 4 for division\npress 0 for quit\n"))
    if inpt==0:
        exit()
    match inpt:
        case 1:
            a =int(input("enter first number for addition\n"))
            b =int(input("enter second number for addition\n"))
            print("result = ",a+b,"\n")
        case 2:
            a =int(input("enter first number for substraction\n"))
            b =int(input("enter second number for substraction\n"))
            print("result = ",a-b,"\n")
        case 3:
            a =int(input("enter first number for multiplication\n"))
            b =int(input("enter second number for multiplication\n"))
            print("result = ",a*b,"\n")
        case 4:
            a =int(input("enter first number for division\n"))
            b =int(input("enter first number for division\n"))
            print("result = ",a/b,"\n")


