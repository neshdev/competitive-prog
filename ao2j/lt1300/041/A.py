n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

cycles = 0
for i in range(1, m):
    if arr[i-1] > arr[i]:
        cycles += 1

ringroad = cycles*n+arr[-1]-1
print(ringroad)

