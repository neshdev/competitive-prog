def shorten(word):
    if len(word) > 10:
        return f"{word[0]}{len(word)-2}{word[-1]}"
    else:
        return word

n = int(input())
out = []
for _ in range(n):
    word = input()
    ans = shorten(word)
    out.append(ans)

print("\n".join(out))
