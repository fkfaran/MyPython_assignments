arr = [1,2,5,2,7,1,3,9,6,3]


for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==arr[j] and i!=j:
            arr.remove(arr[j])
print(arr)
# while i<len(arr):
#     j=0
#     while j<len(arr):
#         if i!=j and arr[i]==arr[j]:
#             break
#         j+=1
#     if j==len(arr):
#         a2.append(arr[i])
#     i+=1
# print(a2)

    


