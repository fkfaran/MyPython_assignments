"""5. Write a python script which takes a three digit number from the user and displays
only its first digit."""

a = 523

while True:
    a =a//10
    if a//10==0:
        break
print(a)