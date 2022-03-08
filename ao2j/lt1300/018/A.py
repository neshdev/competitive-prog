n = int(input())
arr = [int(x) for x in input().split()]    

hi_count = 0
lo_count = 0
hi = arr[0]
lo = arr[0]
for i in range(1,n):
    if arr[i] > hi:
        hi = arr[i]
        hi_count += 1
    
    if arr[i] < lo:
        lo = arr[i]
        lo_count += 1

print(hi_count + lo_count)