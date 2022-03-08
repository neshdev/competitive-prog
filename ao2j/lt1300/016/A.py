k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())


dp = [False]*(d+1)
for x in [k,l,m,n]:
    for i in range(x, d+1, x):
        dp[i] = True

ans = dp.count(True)
print(ans)