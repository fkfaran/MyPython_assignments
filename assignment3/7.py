"""7. Write a python script to store binary number 1100101 in a variable and print it in
decimal format."""

a =1100101
i=0
num =0
while a:
    b = a%10
    if b==1:
        num =num+2**i
    i+=1
    a=int(a/10)
print(num)
