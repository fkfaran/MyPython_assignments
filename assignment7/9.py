"""9. Write a python script to check whether a given year is a leap year or not."""
a =int(input("enter a year to check leap year\n"))
if a%100==0:
    print("leap year") if a%400==0 else print("year is not a leap year")
elif a%4==0:
    print("year is a leap year")
else:
    print("year is not a leap year")