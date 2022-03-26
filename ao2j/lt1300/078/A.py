y, k, n = [int(x) for x in input().split()]

x_hi = n-y
out = []
x = 0
K = k
while x < x_hi:
    # print(k, k-y)
    x = K - y
    if x > 0:
        out.append(str(x))
    K += k
if out and x > x_hi:
    out.pop()

# out = map(str, out)
if out:
    print(" ".join(out))
else:
    print("-1")