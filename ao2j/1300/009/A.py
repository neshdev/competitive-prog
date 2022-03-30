n = int(input())

bags = n*n

arr = [i+1 for i in range(bags)]

i = 0
j = len(arr)-1

out = []
while i < j:
    x = arr[i]
    y = arr[j]
    out.append(f"{x} {y}")

    i += 1
    j -= 1

print("\n".join(out))