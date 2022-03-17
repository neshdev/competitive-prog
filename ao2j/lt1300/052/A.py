s = input()

N = len(s)
count = 0
player = s[0]
msg = "NO"
for i in range(N):
    if s[i] == player:
        count += 1
    else:
        player = s[i]
        count = 1
    if count >= 7:
        msg = "YES"
        break

print(msg)