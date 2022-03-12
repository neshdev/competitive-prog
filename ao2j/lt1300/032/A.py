from collections import deque

n,m = [int(x) for x in input().split()]
arr = [(int(x),i+1) for i,x in enumerate(input().split())]
while arr:
    new = []
    for i in range(len(arr)):
        x,idx = arr[i]
        if x - m > 0:
            new.append((x-m, idx))
    arr = new

print(idx)

