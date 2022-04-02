n, k = [int(x) for x in input().split()]

ps = [str(i+1) for i in range(n)]

front = ps[:(n-k-1)]
back = ps[-k-1:][::-1]

xs = front + back

print(" ".join(xs))