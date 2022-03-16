n = input()

if len(n) == 1:
    if n[0] == "1":
        print("YES")
    else:
        print("NO")
if len(n) == 2:
    if n == "14" or n == "11":
        print("YES")
    else:
        print("NO")
if len(n) > 2:
    arr = list(n)
    N = len(n)
    i = 0
    msg = "YES"
    while i < N:
        if i+2 < N and arr[i] == "1"  and arr[i+1] == "4" and arr[i+2] == "4":
            i += 3
        elif i+1 < N and arr[i] == "1"  and arr[i+1] == "4":
            i += 2
        elif arr[i] == "1":
            i += 1
        else:
            msg = "NO"
            break
    print(msg)