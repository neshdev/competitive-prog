def permute(arr, N):
    found = {x+1: False for x in range(N)}
    for x in arr:
        while x:
            if x in found and found[x] == False:
                found[x] = True
                break
            x //= 2
        
    return "YES" if all(found.values()) else "NO"


t = int(input())

for _ in range(t):
    N = int(input())
    arr = [int(x) for x in input().split()]
    ans = permute(arr, N)
    print(ans)
