n = int(input())
arr = [int(x) for x in input().split()]

q,r = divmod(n, sum(arr))
pages = r
if r == 0:
    pages = sum(arr)
total = 0
for i in range(7):
    if total + arr[i] >= pages:
        break
    total += arr[i]



print(i+1)