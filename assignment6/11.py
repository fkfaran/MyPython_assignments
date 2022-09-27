"""11. Write a python script to take the month value in numeric format and display the
number of days in it."""



month = int(input("enter month\n"))
if month in (1,3,5,7,8,10,12):
    print("total 31 days in this month")
elif month in (4,6,9,11):
    print("total 30 days in this month")
else:
    print("total 28 days in this month") 