from re import I


n = int(input())

if n == 1:
    print("1")
if 1 < n <= 3:
    print("NO SOLUTION")
elif n == 4:
    print("3 1 4 2")
else:
    ans = []
    for x in range(n,0,-2):
        ans.append(x)
    for x in range(n-1,0,-2):
        ans.append(x)
    ans = map(str, ans)
    print(" ".join(ans))