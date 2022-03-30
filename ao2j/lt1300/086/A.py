n, k = [int(x) for x in input().split()]
arr = []
for _ in range(n):
    p, t = [int(x) for x in input().split()]
    arr.append((p,t))

arr.sort(key = lambda x: (x[0], -x[1]), reverse=True)
# print(arr)

ranks = [1]*n
for i in range(1, n):
    if arr[i] == arr[i-1]:
        ranks[i] = ranks[i-1]
    else:
        ranks[i] = ranks[i-1] + 1

from collections import Counter
freq = Counter(ranks)

# print(list(zip(ranks, range(n))))

out = freq.get(ranks[k-1])
print(out)