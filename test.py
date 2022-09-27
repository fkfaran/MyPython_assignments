s = "repeating"
t =""
p =""
n =0
while n<len(s):
    if s[n] not in t:
        t+=s[n]
    else:
        if len(t)>len(p):
            p=t
        t=s[n]
        # t=""
    n+=1
else:
    if len(t)>len(p):
        p=t
print(p)
































# s = "geeeekfgssaaaforaageeks"
# t =''
# temp =''
# n =1
# while n<len(s)-1:
#     if s[n-1]!=s[n] and s[n]!=s[n+1]:
#         temp +=s[n]
#     else:
#         if len(temp)>len(t):
#             t=temp
#         temp = ''
        
#     n+=1
# else:
#     if len(temp)>len(t):
#         t =temp+s[-1]


# print(t)