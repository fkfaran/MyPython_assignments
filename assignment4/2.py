 
while True:
    try:
        number = int(input("enter number\n"))
        print(f"number is = {number}")
        break
    except :
        print("invalid input\nplease enter a number")
        