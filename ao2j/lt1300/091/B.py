n = int(input())
arr = [int(x) for x in input().split()]

# MAX = 1000
# dp = [[1] for i in range(MAX)]
# for d in range(2,MAX):
#     for i in range(d, MAX, d):
#         dp[i].append(d)

# for i in range(1, MAX):
#     if len(dp[i]) == 3:
#         print(dp[i])

MAX = 1_000_001
# MAX = 11
dp = [True]*MAX
for i in range(4, MAX, 2):
    dp[i] = False

for d in range(3,MAX,2):
    for i in range(2*d, MAX, d):
        dp[i] = False

t_primes = set()
for i in range(2,MAX):
    if dp[i]:
        t_primes.add(i*i)

out = []
for x in arr:
    if x in t_primes:
        out.append("YES")
    else:
        out.append("NO")

print("\n".join(out))