n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

class stack:
    def __init__(self):
        self.xs = []
        self.mins = [float('inf')]
        self.maxs = [float('-inf')]

    @property
    def min(self):
        return self.mins[-1]

    @property
    def max(self):
        return self.maxs[-1]

    def push(self, x):
        self.xs.append(x)
        self.mins.append(min(x, self.mins[-1]))
        self.maxs.append(max(x, self.maxs[-1]))

    def pop(self):
        self.mins.pop()
        self.maxs.pop()
        return self.xs.pop()

    def __len__(self):
        return len(self.xs)

    def __str__(self):
        return f"{self.xs} + mins={self.mins} + maxs={self.maxs}"

def two_pointer(arr, k):
    s1,s2 = stack(), stack()
    N = len(arr)
    total = 0
    l = 0

    def good():
        minimums = min(s1.min, s2.min)
        maximums = max(s1.max, s2.max)
        return maximums - minimums <= k

    def add(x):
        s2.push(x)

    def remove():
        if not len(s1):
            while len(s2):
                s1.push(s2.pop())
        s1.pop()

    for r in range(N):
        add(arr[r])
        # print("adding", s1,"|", s2)
        while not good():
            remove()
            l += 1
            # print("removing", s1,"|", s2)
        total += (r-l+1)
    return total

ans = two_pointer(arr, k)
print(ans)