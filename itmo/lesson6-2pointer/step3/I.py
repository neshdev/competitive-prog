n, s = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


class Stack:
    def __init__(self, S) -> None:
        init = [False]*(S+1)
        init[0] = True
        self.xs = [init]
        self.N = S+1
        self.idxs = []

    def push(self, x):
        N = self.N
        arr = list(self.xs[-1])
        for i in range(N):
            if i - x >= 0:
                arr[i] |= self.xs[-1][i-x]
            else:
                arr[i] = arr[i]
        self.xs.append(arr)
        self.idxs.append(x)

    def pop(self):
        self.xs.pop()
        return self.idxs.pop()

    def possible(self):
        return self.xs[-1][-1]

    def __len__(self):
        return len(self.xs)-1

    def __str__(self):
        return str(list(zip(range(self.N),self.xs[-1])))

def two_pointer(arr, s):
    l = 0
    N = len(arr)
    min_segment = float('inf')

    s1,s2 = Stack(s), Stack(s)

    def add(r):
        s2.push(arr[r])
        # print((l,r))
        # # print(s1)
        # print(arr[r])
        # print(s2)
        # print("=====================")

    def remove():
        if not s1:
            while s2:
                s1.push(s2.pop())
        return s1.pop()

    def evaluate():
        """
        using the fact
        S = A + B
        """
        M = s+1
        for i in range(0,M):
            a = s1.xs[-1][i]
            b = s2.xs[-1][-1-i]
            if a and b:
                return True
        return False


    for r in range(N):
        add(r)
        ok = False
        while evaluate():
            remove()
            l += 1
            ok = True

        if ok:
            min_segment = min(min_segment, r-l+2)
            # print((l-1,r),(r-l+2))
    return min_segment


ans = two_pointer(arr, s)
print(ans)
