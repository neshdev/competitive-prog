n = int(input())
total = 0
for _ in range(n):
    arr = [int(x) for x in input().split()]
    if sum(arr) >= 2:
        total += 1
print(total)
    