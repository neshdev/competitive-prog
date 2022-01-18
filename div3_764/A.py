def plus_one(arr):
    x = min(arr)
    y = max(arr)
    return y - x

t = int(input())
for _ in range(t):
    N = int(input())
    arr  = [int(x) for x in input().split()]
    ans = plus_one(arr)
    print(ans)