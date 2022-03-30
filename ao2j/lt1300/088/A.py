n = 4
arr = []
for _ in range(n):
    s = list(input())
    arr.append(s)


def check(arr, paint='#'):
    possible = False
    Y = len(arr)
    X = len(arr[0])
    for y in range(1, Y):
        for x in range(1, X):
            if arr[y-1][x] == paint and arr[y][x-1] == paint and arr[y-1][x-1] == paint:
                possible = True
                break
    return possible


arr2 = []
for xs in arr:
    arr2.append(list(xs)[::-1])

if check(arr) or check(arr2) or check(arr, '.') or check(arr2, '.'):
    print("YES")
else:
    arr = arr[::-1]
    arr2 = arr2[::-1]
    if check(arr) or check(arr2) or check(arr, '.') or check(arr2, '.'):
        print("YES")
    else:
        print("NO")
