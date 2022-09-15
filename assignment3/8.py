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
