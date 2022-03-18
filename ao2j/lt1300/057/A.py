n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
best = arr[-1] - arr[0] 
for i in range(m-n+1):
    # print(i)
    best = min(arr[i+n-1] - arr[i], best)
print(best)