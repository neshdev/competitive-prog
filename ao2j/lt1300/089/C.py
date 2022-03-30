n = int(input())
arr = [int(x)-1 for x in input().split()]


rem = set(i for i in range(n))
outside = []
for i in range(n):
    if arr[i] in rem:
        rem.remove(arr[i])
    else:
        outside.append(arr[i])

total = 0
rem = sorted(rem)
outside = sorted(outside)

m = len(outside)
for i in range(m):
    total += abs(rem[i] - outside[i])
print(total)
