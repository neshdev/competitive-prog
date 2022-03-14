n = int(input())
arr = [int(x) for x in input().split()]

count_of_5 = arr.count(5)
count_of_0 = len(arr) - count_of_5
if count_of_0 >= 1:
    x = 0
    best = None
    for i in range(count_of_5):
        x += 5
        x %= 9
        if x == 0:
            best = i
    if best:
       arr = ['5']*(best+1) + ['0']*count_of_0
       print("".join(arr))
    else:
        print(0)
    
else:
    print(-1)