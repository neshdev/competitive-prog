n = int(input())
exit, enter = [int(x) for x in input().split()]
total = enter
best = enter
for i in range(1, n):
    x, e = [int(x) for x in input().split()]
    total -= x
    total += e
    best = max(best, total)
print(best)
