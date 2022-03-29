n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

dp = [0]*n
uniq = set()
for i in range(n-1, -1,-1):
    x = arr[i]
    uniq.add(x)
    dp[i] = len(uniq)

out = []
for _ in range(m):
    i = int(input())-1
    out.append(str(dp[i]))


print("\n".join(out))