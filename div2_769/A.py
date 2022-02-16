def abc(s):
    if len(s) == 1:
        return "YES"
    if len(s) == 2:
        if s == "10" or s == "01":
            return "YES"
        return "NO"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    N = input()
    s = input()
    ans = abc(s)
    print(ans)
