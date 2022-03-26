s1 = list(input())
s2 = list(input())

def swap(arr, i,j):
    arr[i], arr[j] = arr[j], arr[i]

def find_and_replace(arr, i, j, x):
    for k in range(i,j):
        if arr[k] == x:
            swap(arr,i,k)
            break

N = len(s1)
M = len(s2)

if N != M:
    print("NO")
else:
    msg = "YES"
    xs = []
    for i in range(N):
        if s1[i] != s2[i]:
            xs.append(i) 

    if len(xs) == 2:
        i,j = xs
        swap(s1, i,j)

    for i in range(N):
        if s1[i] != s2[i]:
            msg = "NO"
            break
    print(msg)



