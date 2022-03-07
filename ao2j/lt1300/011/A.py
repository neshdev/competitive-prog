n,m = [int(x) for x in input().split()]

N = 100
dp = [1]*100

for x in range(2, N):
    for i in range(2*x,N,x):
        dp[i] = 0


for i in range(n+1,m+1):
    if dp[i]:
        break        
# print(dp, i)

if i == m and dp[m]:
    print("YES")
else:
    print("NO")
        