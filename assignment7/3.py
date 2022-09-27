"""3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""

while True:
    choice = int(input("""enter choice\npress 1 for checking isosceles triangle\npress 2 for checking right angle triangle\n
    press 3 for checking equilateral triangle\npress 4 for exit"""))
    a=int(input("enter first number\n"))
    b=int(input("enter second number\n"))
    c=int(input("enter third number\n"))
    match choice:
        case 3:
            if a==b==c:
                print("numbers are making equilateral triangle")
        case 2:
            if a==b or b==c or c==a:
                print("numbers make a isosceles triangle")
            else:
                print("numbers does not make a isosceles triangle")
        case 3:
            a= a**2
            b= b**2
            c= c**2
            if a==b+c or b==a+c or c==a+b:
                print("numbers are making Right angle triangle")
        case 4:
            exit()


