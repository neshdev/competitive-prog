from re import L


arr1 = input()
arr2 = input()

N  = len(arr1)

out = [None]*N
for i in range(N):
    out[i] = "0" if arr1[i] == arr2[i] else "1"

print("".join(out))