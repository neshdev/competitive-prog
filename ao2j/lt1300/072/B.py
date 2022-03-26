n = int(input())
arr = []
best_length = -1
best_lo = None
best_hi = None
best_idx = 0
for i in range(n):
    lo, hi = [int(x) for x in input().split()]
    if hi-lo > best_length:
        best_length = hi-lo
        best_lo = lo
        best_hi = hi
        best_idx = i+1
    arr.append([lo,hi])

overlaps = True
for l,h in arr:
    overlaps &= best_lo <= l <= h <= best_hi

if overlaps:
    print(best_idx)
else:
    print("-1")