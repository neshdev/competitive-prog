n = int(input())
arr = [int(x) for x in input().split()]

lo = min(arr)

count = 0
pos = 0
for i in range(n):
    if arr[i] == lo:
        count += 1
        pos = i

if count > 1:
    print("Still Rozdil")
else:
    print(pos+1)