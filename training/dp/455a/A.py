n = int(input())
arr = [int(x) for x in input().split()]

L = min(100_000, max(arr))
counts = [0]*(L+1)
for x in arr:
    counts[x] += 1

a = 0
b = counts[1]
c = counts[2]*2 if L > 1 else b
best = max(a,b,c)
for i in range(L+1):
    if i-3 >= 0:
        a,b,c = b,c,max(a,b) + i*counts[i]
        best = max(best, c)

print(best)



