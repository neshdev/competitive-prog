"""
This is not the right solution
"""

n, x = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

arr.sort()

for i in range(n):
    if arr[i] > x:
        print("0")
        exit()

allowed = 0
total = 0
count = 0
for i in range(n):
    if arr[i] + total <= x and count+1 <= 2:
        total += arr[i]
        count += 1
    else:
        allowed += 1
        total = arr[i]
        count = 1
allowed += 1

print(allowed)


# 2 3 7 9
# 2 3 | 7 | 9

# 10 15
# 5 7 | 8 | 8 | 8 | 8 | 9 | 9 | 10 | 10
# 5 10 | 7 8 | 8 | 8 | 8 | 9 | 9 | 10
