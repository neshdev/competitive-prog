Y,X = [int(x) for x in input().split()]
arr = []
for _ in range(Y):
    row = list(input())
    arr.append(row)

rows = set(i for i in range(Y))
cols = set(i for i in range(X))

for y in range(Y):
    for x in range(X):
        if arr[y][x] == "S":
            if y in rows:
                rows.remove(y)
            if x in cols:
                cols.remove(x)


score = 0
for y in rows:
    for x in range(X):
        if arr[y][x] == ".":
            score += 1
            arr[y][x] = None


for x in cols:
    for y in range(Y):
        if arr[y][x] == ".":
            score += 1
            arr[y][x] = None

print(score)
