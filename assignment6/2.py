"""2. Write a python script to check whether a given number is divisible by 5 or not"""

number = int(input("enter a number\n"))
if number%5==0 and number is not 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")