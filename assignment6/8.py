"""8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""

a = int(input("enter first constant of quadratic equation\n"))
b = int(input("enter second constant of quadratic equation\n"))
c = int(input("enter third constant of quadratic equation\n"))
d =b**2-4*a*c
if d>0:
    print("roots are real and distinct")
elif d<0:
    print("roots are complex and distinct")
else:
    print("roots are real and equal")
