n,a,b,c = [int(x) for x in input().split()]

dp = [-1]*(n+1)
dp[0]= 0
for x in set([a,b,c]):
    for i in range(1,n+1):
        if i-x >= 0 and dp[i-x] >= 0:
            dp[i] = max(dp[i-x] + 1, dp[i])
    # print(dp)

print(dp[-1])

# print(max(dp))


#     0   1   2   3   4   5
# 2   1       1       1
# 3               1       2
# 5                       1