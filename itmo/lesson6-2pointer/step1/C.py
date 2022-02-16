def merge(n,m,arr1,arr2):
    count = 0
    i = 0
    j = 0
    while j < m:
        while i < n and arr1[i] < arr2[j]:
            i += 1

        total = 0
        while i < n and arr1[i] == arr2[j]:
            total += 1
            i += 1

        factor = 1
        while j+1 < m and arr2[j]==arr2[j+1]:
            factor += 1
            j += 1

        count += total*factor
        j += 1
    return count

n, m = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
n, m = len(arr1), len(arr2)

if n < m:
    n,m,arr1,arr2 = m,n,arr2,arr1

ans = merge(n,m, arr1, arr2)
print(ans)


"""
Ex1:

1 1 3 3 3 5 8 8
1 3 3 4 5 5 5

    2       3 3     1 1 1
    *       * *     * * *
1 1 1 3 3 3 3 3 4 5 5 5 5
"""