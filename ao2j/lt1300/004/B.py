arr = input()
N = len(arr)
out = []
i = 0
while i < N:
    if arr[i] == ".":
        out.append("0")
        i += 1
    elif arr[i] == "-" and arr[i+1] == ".":
        out.append("1")
        i += 2
    elif arr[i] == "-" and arr[i+1] == "-":
        out.append("2")
        i += 2

print("".join(out))