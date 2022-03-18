s = input()
word = 'hello'
i = 0
for c in s:
    if i < 5 and c == word[i]:
        i += 1

if i >= len(word):
    print("YES")
else:
    print("NO")