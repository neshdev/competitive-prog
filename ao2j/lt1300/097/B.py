from collections import Counter
n, k = [int(x) for x in input().split()]
arr = input() 

freq = Counter(list(arr))

items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# print(items)
N = len(items)
total = 0
for i in range(N):
    c, count = items[i]
    removed = min(k, count)
    total += removed**2
    k -= removed
    if k == 0:
        break

print(total)
