for y in range(5):
    arr = [int(x) for x in input().split()]
    for x in range(5):
        if arr[x] == 1:
            res = abs(2-x)
            res += abs(2-y)
            print(res)