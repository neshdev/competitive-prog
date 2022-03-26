happy = []
for i in range(5):
    happy.append([int(x) for x in input().split()])

def next_permutation(xs):
    N = len(xs)
    i = N-2
    while i and xs[i] > xs[i+1]:
        i -= 1
    # print(arr, i)
    best = xs[i]
    best_pos = i
    for j in range(i, N):
        if xs[j] > best:
            best = xs[i]
            best_pos = j
    # print(arr, best_pos, best)
    
    swap(xs, i, best_pos)
    reverse(xs, i+1, N-1)
    return xs

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def reverse(arr,i,j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def all_permutations(n):
    arr = list(range(n))
    prod = 1
    for i in range(1,n+1):
        prod *= i
 
    for i in range(prod):
        yield arr
        arr = next_permutation(arr)

from collections import deque
best = float('-inf')
for p in all_permutations(5):
    N = len(p)
    # print("perm =", p)
    total = 0 
    for k in range(N):
        ps = deque(p[k:])
        
        # print(ps)
        while len(ps) >= 2:
            i = ps.popleft()
            j = ps.popleft()
            total += happy[i][j]
            total += happy[j][i]
            # print(i,j,happy[i][j], happy[j][i])
    best = max(best, total)

print(best)
# print(happy)