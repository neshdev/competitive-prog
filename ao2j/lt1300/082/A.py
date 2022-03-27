n = int(input())
n_sq = n**2
total = 0

possible = set()
for i in range(n+1):
    possible.add(i*i)

for a in range(1,n+1):
    for b in range(a, n+1):
        c_sq = a**2 + b**2
        if c_sq in possible:
            total += 1
            # print(a,b,c_sq**(1/2))

print(total)