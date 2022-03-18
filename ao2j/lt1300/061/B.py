n = int(input())
arr = [int(x) for x in input().split()]

lo = min(arr)
hi = max(arr)
a = arr.count(lo)
b = arr.count(hi)
prod = a*b
if lo == hi:
    prod = a * (a-1) // 2
print(f"{hi - lo} {prod}")