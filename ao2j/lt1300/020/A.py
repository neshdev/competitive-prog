arr = [int(x) for x in input().split('+')]
arr.sort()
arr = map(str, arr)
print("+".join(arr))