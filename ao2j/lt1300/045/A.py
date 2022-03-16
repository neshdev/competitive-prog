n = int(input())
xs = [int(x) for x in input().split()]
m = int(input())
ys = [int(x) for x in input().split()]

N = max(max(xs), max(ys))

factors = [[1] for i in range(N+1)]
# factors[1].append(1)
for m in range(2,N+1):
    for i in range(m, N+1, m):
        factors[i].append(m)

# print(factors)

highest_ratio = 1
count = 0
divisors = set(xs)
for b in ys:
    for x in factors[b]:
        if x in divisors:
            # print(b,x)
            if highest_ratio == b // x:
                count += 1
            elif highest_ratio <  b // x:
                highest_ratio = b // x
                count = 1
print(count)

