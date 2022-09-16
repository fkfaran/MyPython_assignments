"""5. Write a python script which takes a three digit number from the user and displays
only its first digit."""

a = 94323

while True:
    a =int(a/10)
    if int(a/10)==0:
        break
print(a)