def can_make(s, c):
    found = False
    for i,char in enumerate(s):
        if char == c and i % 2 == 0:
            found = True

    if found:
        return "YES"
    else:
        return "NO"


n = int(input())
out = []
for _ in range(n):
    s = input()
    c = input()
    ans = can_make(s,c)
    out.append(ans)

print("\n".join(out))