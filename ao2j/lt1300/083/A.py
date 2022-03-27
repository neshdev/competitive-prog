"""
tried mergesort but took too long (TLE)
Instead, we did counting sort (Accepted)
"""

with open('input.txt', 'r') as f:
    n = int(f.readline())
    arr = [int(x) for x in f.readline().split()]

    MAX = 5001
    dp = [[] for _ in range(MAX)]
    for i,x in enumerate(arr):
        dp[x].append(i)

    error = False
    with open('output.txt', 'w') as W:
        out = []
        for i in range(1,MAX):
            if dp[i]:
                if len(dp[i]) % 2 == 0:
                    xs = dp[i]
                    while xs:
                        i,j = xs.pop(), xs.pop()
                        item = f"{i+1} {j+1}"
                        out.append(item)
                else:
                    error = True
                    break

        if error:
            W.write("-1")
        else:

            W.write("\n".join(out))