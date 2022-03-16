n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

arr.sort()

total = 0
for i in range(k):
    if arr[i] < 0:
        total += -arr[i]
print(total)
