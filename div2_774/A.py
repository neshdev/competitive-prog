t = int(input())

out = []
for _ in range(t):
    n,s = [int(x) for x in input().split()]
    q = s // (n*n)
    out.append(q)

out = map(str, out)
print("\n".join(out))