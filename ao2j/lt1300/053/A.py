s = input()
rem = [c.lower() for c in s if c.lower() not in {'a', 'e', 'i', 'o', 'u', 'y'}]
ans =  "." + ".".join(rem)
print(ans)