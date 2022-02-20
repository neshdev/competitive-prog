import re


n,m = [int(x) for x in input().split()]
s = input()
cards = input()



def two_pointer(s,cards):
    N = len(s)
    counter = [0]*26
    global total_chars
    total_chars = len(cards)
    for c in cards:
        i = ord(c) - ord('a')
        counter[i] +=1
    
    l = 0
    def good(i):
        idx = ord(s[i]) - ord('a')
        return total_chars >= 0 and counter[idx] >= 0

    def add(i):
        global total_chars
        idx = ord(s[i]) - ord('a')
        counter[idx] -= 1
        total_chars -= 1

    def remove(i):
        global total_chars
        idx = ord(s[i]) - ord('a')
        counter[idx] += 1
        total_chars += 1

    out = 0
    for r in range(N):
        add(r)
        while not good(r):
            remove(l)
            l += 1
        out += r-l+1

    return out


ans = two_pointer(s,cards)
print(ans)