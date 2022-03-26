xs = list(input())
N = len(xs)
pos = N-1
for i in range(N):
    if xs[i] == '0':
        pos = i
        break
xs.pop(pos)

print("".join(xs))