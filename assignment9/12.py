"""12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""

cnum = input("enter complex number\n")
i = cnum.index('+' or '-')
real = int(cnum[:i])
imaginary = int(cnum[i + 1:-1])
if real > imaginary:
    print("greater is = ", real)
else:
    print("greater is = ", imaginary)
