n = int(input())
arr = [int(x) for x in input().split()]

x = n*(n+1) // 2 - sum(arr)
print(x)