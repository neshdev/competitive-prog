n = int(input())
arr = [int(x)-1 for x in input().split()]
 
def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
i=0
for i in range(0,n-1):
    if arr[i] > arr[i+1]:
        break
j=n-1
for j in range(n-1, -1, -1):
    if arr[j-1] > arr[j]:
        break

# print(arr)
reverse(arr, i, j)
# print(i, j, arr)


broken = False
for k in range(1,n):
    if arr[k-1] > arr[k]:
        broken = True

if broken:
    print("no")
elif i >= j:
    print("yes")
    print("1 1")
else:
    print("yes")
    print(f"{i+1} {j+1}")
