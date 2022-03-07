n = int(input())
out = [i+1 for i in range(n)]
if n % 2 == 0:
    for i in range(0,n,2):
        out[i], out[i+1] = out[i+1], out[i]

    for i in range(n):
        print(out[i], end=' ')
else:
    print("-1")