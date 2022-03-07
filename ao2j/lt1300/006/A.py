arr = []
for i in range(3):
    items = [int(x) for x in input().split()]
    arr.append(items)

Y = len(arr)
X = len(arr[0])

out = [[1 for _ in range(X)] for _ in range(Y)]

def transitions(y,x):
    yield y,x
    yield y,x+1
    yield y,x-1
    yield y+1,x
    yield y-1,x

def valid_transitions(y0,x0):
    for y,x in transitions(y0,x0):
        if 0 <= y < Y and 0 <= x < X:
            yield y,x


for y in range(Y):
    for x in range(X):
        total = 0
        for y1,x1 in valid_transitions(y,x):
            total += arr[y1][x1]
        out[y][x] = 1 if total % 2 == 0 else 0

for xs in out:
    xs = map(str, xs)
    print("".join(xs))