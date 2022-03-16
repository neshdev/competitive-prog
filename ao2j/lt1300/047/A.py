n,m = [int(x) for x in input().split()]

count = 0
for a in range(n+1):
    b = n - a*a
    if b < 0:
        break

    if a + b*b == m:
        count += 1

print(count)