n = int(input())
arr = [int(x) for x in input().split()]

hi = 0
maximum = float('-inf')
for i in range(n):
    if maximum < arr[i]:
        hi = i
        maximum = arr[i]

lo = n-1
minimum = float('inf')
for i in range(n-1,-1,-1):
    if minimum > arr[i]:
        lo = i
        minimum = arr[i]

# print(lo, hi)

total = hi+(n-lo-1)
if hi > lo:
    total -= 1
print(total)