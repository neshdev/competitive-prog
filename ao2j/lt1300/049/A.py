s = input()

out = []
N = len(s)
i = 0
while i < N:
    if s[i:i+3] == "WUB":
        i += 3
        if out and out[-1] != " ":
            out.append(" ")
    else:
        out.append(s[i])
        i += 1
print("".join(out))