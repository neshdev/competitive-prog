n,k = [int(x) for x in input().split()]

q,r = divmod(n,2)
if r:
    n += 1
q,r = divmod(n,2)
if k <= q:
    print(k*2-1)
else:
    print((k-q)*2)