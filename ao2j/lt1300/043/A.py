arr1 = input()
arr2 = input()

if len(arr1) != len(arr2):
    print("NO")
else:
    i = 0
    j = len(arr1)-1
    msg = "YES"
    while i < len(arr1):
        if arr1[i] == arr2[j]:
            i += 1
            j -= 1
        else:
            msg = "NO"
            break
    print(msg)