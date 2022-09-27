"""10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""

a = int(input("enter first number\n"))
b = int(input("enter second number\n"))
c = int(input("enter third number\n"))
(print("greater is = ",a) if a>c else print("greater is = ",c)) if a>b else (print("greater is = ",b) if b>c else print("greater is = ",c))