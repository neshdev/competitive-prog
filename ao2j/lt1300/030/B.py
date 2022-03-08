"""
n = len(arr)
q = # of queries
Finished this using binary search. time = O(n log n + q log n), space = O(1)
Can also use bucket sort. time=O(n + q), space = O(1)

"""
n = int(input())
arr = [(i, int(x)) for i,x in enumerate(input().split())]

arr.sort(key=lambda x: x[1])

def find(arr, x):
    l = 0       # f(x) <= x
    r = len(arr)   # f(x) > x
    while r > l + 1:
        m = (l + r) // 2
        if arr[m][1] <= x:
            l = m
        else:
            r = m
    return l

A,B=0,0
# print(arr)
q = int(input())
queries = [int(x) for x in input().split()]
for i in range(q):
    x = queries[i]
    pos = find(arr, x)
    idx = arr[pos][0]
    A_cmp = 1+idx
    B_cmp = n-idx
    # print("ans",x,n,f"{pos=}", idx, A_cmp, B_cmp)
    A += A_cmp
    B += B_cmp

print(f"{A} {B}")

