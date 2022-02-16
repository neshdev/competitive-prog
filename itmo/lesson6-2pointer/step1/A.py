def merge(n,m, arr1,arr2):
    out = [None]*(n+m)
    i = 0
    k = 0
    for j in range(m):
        while i < n and arr1[i] < arr2[j]:
            out[k] = arr1[i]
            k += 1
            i += 1
        out[k] = arr2[j]
        k += 1
    
    while i < n:
        out[k] = arr1[i]
        k += 1
        i += 1

    return out


n, m = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

if n > m:
    n,m = m,n
    arr1,arr2 = arr2, arr1

for x in merge(n,m, arr1, arr2):
    print(x, end=' ')