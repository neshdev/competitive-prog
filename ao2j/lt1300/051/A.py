n,a,b = [int(x) for x in input().split()]

arr = [True]*(n+1)
for i in range(a+1):
    arr[i] = True

for i in range(a+1,n+1):
    if n-i <= b:
        arr[i] = False

# print(arr)

total = arr.count(False)
print(total)
