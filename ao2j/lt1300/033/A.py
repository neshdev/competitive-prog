n = int(input())
arr = []
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    arr.append((x, y))


def superpoints(arr):

    xs = sorted(arr, key=lambda x: (x[0], x[1]))
    ys = sorted(arr, key=lambda x: (x[1], x[0]))

    lookup = {}
    for i,(x,y) in enumerate(ys):
        lookup[(x,y)] = i

    count = 0
    # print(arr)
    for i in range(n):
        x, y = xs[i]

        if i-1 >= 0 and i+1 < n:
            if xs[i-1][0] == x and xs[i+1][0] == x:
                j = lookup[(x,y)] 
                # print((x,y), i)
                if j-1 >= 0 or j+1 < n:
                    if ys[j-1][1] == y and ys[j+1][1] == y:
                        count += 1 
    return count
ans = superpoints(arr)
print(ans)