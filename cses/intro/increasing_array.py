n = int(input())
arr = [int(x) for x in input().split()]

N = len(arr)
total = 0
for i in range(1, N):
    if arr[i-1] > arr[i]:
        total += arr[i-1] - arr[i]
        arr[i] = arr[i-1]

print(total)
