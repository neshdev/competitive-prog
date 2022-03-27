with open('input.txt', 'r') as f:
    s = f.readline()
    n,m = [int(x) for x in s.split()]
    out = []
    if n > m:
        while n + m:
            if n:
                out.append("B")
                n -= 1
            if m:
                out.append("G")
                m -= 1
    else:
        while n + m:
            if m:
                out.append("G")
                m -= 1
            if n:
                out.append("B")
                n -= 1

ans = "".join(out)
with open("output.txt", 'w') as f:
    f.write(ans)