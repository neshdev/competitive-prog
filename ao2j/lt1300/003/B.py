n,t = [int(x) for x in input().split()]
arr = list(input())

while t:
    temp = [arr[0]]
    for i in range(1,n):
        temp.append(arr[i])
        if arr[i-1] == 'B' and arr[i] == 'G':
            temp[i-1], temp[i] = temp[i], temp[i-1]
    arr = temp
    t -= 1

print("".join(arr))