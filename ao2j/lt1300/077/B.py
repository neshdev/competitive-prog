n = int(input())
if n == 1:
    print(1)
else:
    arr = [int(x) for x in input().split()]
    arr.sort()

    r = sum(arr) % n
    # print(arr)
    if r == 0:
        print(n)
    else:
        print(n-1)