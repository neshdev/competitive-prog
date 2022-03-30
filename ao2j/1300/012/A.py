n,k = [int(x) for x in input().split()]
best = float("-inf")
for _ in range(n):
    f, t = [int(x) for x in input().split()]

    best = max(best, f - (t - k) if t > k else f)
    

print(best)
