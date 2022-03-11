def max_div_mod(l,r,a):
    if l == r:
        q,r = divmod(l,a)
        return q + r
    else:
        lo_q, lo_r = divmod(l, a)
        hi_q, hi_r = divmod(r, a)
        if hi_q - lo_q >= 1:
            return max(hi_q-1 + a-1, hi_q + hi_r)
        else:
            return lo_q + r % a

n = int(input())
out = []
for _ in range(n):
    l,r,a = [int(x) for x in input().split()]
    ans = max_div_mod(l,r,a)
    out.append(ans)

out = map(str, out)
print("\n".join(out))