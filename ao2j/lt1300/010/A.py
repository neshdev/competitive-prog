n = int(input())
arr = input()

count = 0
total = 1
for i in range(1,n):
    if arr[i] == arr[i-1]:
        total += 1
    else:
        count += total-1
        total = 1
count += total-1

print(count)