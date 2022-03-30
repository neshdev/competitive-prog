n = int(input())
arr = [int(x) for x in input().split()]
X = sum(arr)
count = 0
for x in arr:
    if (X - x) % 2 == 0:
        count += 1

print(count)