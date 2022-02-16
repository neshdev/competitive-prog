"""
find | {(l,r) | sum a[l..r] >= s } |


Adding any number will hold the following invariant

smaller segment l..r to larger segment L..R

        l            r
        --------------
    L                       R
    -------------------------

This holds the invariant:

sum a[l..r] >= s

sum a[L..R] >= s where L <= l <= r <= R

because adding any element to a[l..r] will still be >= s.

Since, sum a[L..R] >= s indicates where all such segments will be true.
To count additional elements

adding any range from 0<=i<=L-1 will also hold the invariance

sum a[i..L-1] + sum a[L..R] >= s
where 0<=i<=L-1


0       L-1  L        R
        <s   >=s
---------- | --------------

"""
#     l   r
# 2 6 4 3 6 8 9


def two_pointer(arr, s):
    N = len(arr)
    l = 0
    total = 0

    count = 0

    for r in range(N):
        total += arr[r]
        while total >= s:

            total -= arr[l]
            l += 1

        # print(l,r)
        count += l

    return count


n, s = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


ans = two_pointer(arr, s)
print(ans)
