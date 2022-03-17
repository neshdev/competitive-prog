n = int(input())

arr = list(range(n))

def sort(x):
    if x == 0:
        return
    arr[x], arr[x-1] = arr[x-1], arr[x]
    sort(x-1)

sort(n-1)
for i in range(n):
    print(arr[i]+1, end=" ")