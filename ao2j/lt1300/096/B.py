x,y = [int(x) for x in input().split()]
n = int(input())
mod = 10**9+7
x %= mod
y %= mod
if n == 1:
    print(x)
elif n == 2:
    print(y)
else:
    for i in range((n-2) % 6):
        # print(i, x,y)
        x,y = y, (y-x) % mod
    print(y)