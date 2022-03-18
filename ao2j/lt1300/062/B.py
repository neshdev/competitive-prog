n = int(input())
arr = [int(x) for x in input().split()]
arr = list(enumerate(arr))
arr.sort(key=lambda x: x[1])

ans = [arr[0][0]]
seq = []
out = [arr[0][1]]
for i in range(1,n):
    if arr[i-1][1] == arr[i][1]:
        ans.append(arr[i][0])
    else:
        seq.append(ans)
        ans = [arr[i][0]]
        out.append(arr[i][1])

if ans:
    seq.append(ans)
    out.append(arr[-1][1])


res = []
for k, xs in enumerate(seq):
    # print(out[k], xs)
    diff = 0
    ap = True
    if len(xs) > 1:
        diff = xs[1] - xs[0]
        M = len(xs)
        for i in range(1,M):
            if xs[i] - xs[i-1] != diff:
                ap = False
                break
    if ap:
        res.append(f"{out[k]} {diff}")

print(len(res))
print("\n".join(res))