"""
another way to do this
expand each row
[4 2 4]
as 
1 2 3 4 | 1 2 | 1 2 3 4
then sort
1 1 1 2 2 2 3 3 4
lo will be from left
hi will be from right
"""

from heapq import heapify, heappush, heappop
N,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
# print(arr)

min_arr = []
for x in arr:
    heappush(min_arr, (x,x)) 

n = N
lo = 0
while n:
    k, x = heappop(min_arr)
    # print(x)
    new = x-1
    if new > 0:
        heappush(min_arr, (new,new))
    n -= 1
    lo += x


max_arr = []
for y in arr:
    heappush(max_arr, (-y,y))

hi = 0
while N:
    k,x = heappop(max_arr)
    # print("hi item",x)
    new = x-1
    if new > 0:
        heappush(max_arr, (-new, new))
    N -= 1
    hi += x


print(f"{hi} {lo}")