Y,X,d = [int(x) for x in input().split()]
arr = []
for _ in range(Y):
    xs = [int(x) for x in input().split()]
    arr.extend(xs)

arr.sort()
hi = max(arr)
for i in range(Y*X):
    arr[i] -= hi

if all(map(lambda x: x % d == 0, arr)):
    total = 0
    med = arr[(Y*X) // 2]
    # print(med)
    for x in arr:
        rem = abs(med-x)
        total += rem // d
    print(total)

else:
    print("-1")
