"""6. Write a python script to check whether a given number is a three digit number or not."""

number = int(input("enter a number\n"))
if number >99 and number<1000:
    print("number has three digits")
else:
    print("number has not three digits")