def merge(n,m,arr1,arr2):
    out = [None]*m
    i = 0
    for j in range(m):
        while i < n and arr1[i] < arr2[j]:
            i += 1
        out[j] = i
    return out


n, m = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
n, m = len(arr1), len(arr2)

for x in merge(n,m, arr1, arr2):
    print(x, end=' ')