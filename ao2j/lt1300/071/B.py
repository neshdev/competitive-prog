n = int(input())


MAX = 1_299_828
# MAX = 100
dp = [True]*MAX
for i in range(2*2,MAX,2):
    dp[i] = False

for d in range(3,MAX,2):
    for i in range(2*d, MAX, d):
        dp[i] = False

# print(dp)
arr = []
i = 2
while n and i < MAX:
    if dp[i] == True:
        arr.append(i)
        n -= 1
    i += 1

arr = map(str, arr)
print(" ".join(arr))