a,b,c = [int(x) for x in input().split()]

mod = 2**30
MAX = min(a*b*c+1,1_000_001)
divisors = [1 for i in range(MAX)]

for i in range(2, MAX):
    for d in range(i,MAX, i):
        divisors[d] += 1

total = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            prod = (i+1)*(j+1)*(k+1)
            total += divisors[prod]
            total %= mod

print(total)