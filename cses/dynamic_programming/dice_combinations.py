n = int(input())
mod = 10**9 + 7
dp = [0]*(n+1)
dp[0] = 1

# for dice in [1,2,3,4,5,6]:
#     for x in range(dice, n+1):
#         dp[x] += dp[x-dice]
#     print(dp)
for x in range(n+1):
    for dice in [1, 2, 3, 4, 5, 6]:
        if x-dice >= 0:
            dp[x] += dp[x-dice]
    # print(dp)

print(dp[-1] % mod)
