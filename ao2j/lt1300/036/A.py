n = int(input())
arr = [int(x) for x in input().split()]
# arr.sort(key=lambda x: x[1])
# print(arr)
best = abs(arr[1] - arr[0])
sol1 = 1
sol0 = 0
for i in range(1,n):
    x = abs(arr[i] - arr[i-1])
    # print(x)
    if x < best:
        best = x
        sol1 = i
        sol0 = i-1

x = abs(arr[-1] - arr[0])
# print(x)
if x < best:
    best = x
    sol1 = n-1
    sol0 = 0

print(f"{sol1+1} {sol0+1}")


