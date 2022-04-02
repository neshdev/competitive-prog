n, k = [int(x) for x in input().split()]

if n == 1:
    print(k)
else:
    arr =[[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        arr[i][i] = k-1
        if i+1 < n:
            arr[i+1][i] = 1

    arr[0][-1] = 1

    arr = [" ".join([str(x) for x in xs]) for xs in arr]
    # print(arr)
    print("\n".join(arr))