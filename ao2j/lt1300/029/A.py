n = int(input())
x = 0
for _ in range(n):
    arr = input()
    if arr[1] == "+":
        x += 1
    if arr[1] == "-":
        x -= 1

print(x)