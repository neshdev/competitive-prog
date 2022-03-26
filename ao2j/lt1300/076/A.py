n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
brr = [int(x) for x in input().split()]

x = min(arr)
y = max(arr)
M = min(brr)
if x*2 < M and y < M:
    print(max(y, x*2))
else:
    print(-1)