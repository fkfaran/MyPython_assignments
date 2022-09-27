"""6. Write a python script which takes a three digit number from the user and displays
only its middle digit."""

number = int(input("enter three digit number\n"))

number =number//10
print(number%10)