n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


total = 0
best = float('inf')
j = 0
l = 0
def add(i):
    global total
    total += arr[i]

def remove(i):
    global total
    total -= arr[i]

def good(i,j):
    return j - i + 1 < k

for r in range(n):
    add(r)
    while not good(l,r):
        remove(l)
        l += 1
    if l > 0:
        if best > total + arr[l-1]:
            best = min(best, total + arr[l-1])
            j = l-1

print(j+1)



