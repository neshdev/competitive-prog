from collections import deque


def solve(arr, n):
    out = [0]*n
    for x in range(n-1,0,-1):
        shift = 0
        for i in range(len(arr)):
            if arr[i] == x:
                if i == x:
                    shift = 0
                else:
                    shift = i+1
                break
        temp = []
        for i in range(shift, len(arr)):
            temp.append(arr[i]) 
        for i in range(0, shift-1):
            temp.append(arr[i])
        arr = temp
        out[x] = shift
        if not shift:
            temp.pop()


        # print(arr)
        # print(out)
        # print("----")
    out = map(str, out)
    return " ".join(out)


# 4 7 0 2 1 5 3 6 4 7               

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    arr = [int(x)-1 for x in input().split()]
    ans = solve(arr, n)
    out.append(ans)
print("\n".join(out))
