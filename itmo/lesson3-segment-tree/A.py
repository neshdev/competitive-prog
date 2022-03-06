"""
Store values in intermediate nodes. 
Didn't need to cascade nodes like update.

Implement separate get function that goes from leaf to root.
"""

class ST:
    def __init__(self, n, merge_fn=lambda x, y: x+y, construct_fn=lambda x: x, default=None):
        x = 1
        while x <= n:
            x *= 2
        self.xs = [default]*(2*x)
        self.size = x
        self.merge_fn = merge_fn
        self.construct_fn = construct_fn
        self.default = default

    def build(self, xs):
        i = len(self.xs) // 2 - 1
        j = i-1
        for x in xs:
            self.xs[i] = self.construct_fn(x)
            i += 1

        for i in range(j, -1, -1):
            a = self.xs[i*2+1]
            b = self.xs[i*2+2]
            self.xs[i] = self.merge_fn(a, b)

    def setx(self, x, val):
        """
        set x within 0 <= x < r
        """
        x += (self.size - 1)
        self.xs[x] = self.construct_fn(val)
        x = (x-1) // 2
        while x:
            a = self.xs[x*2+1]
            b = self.xs[x*2+2]
            self.xs[x] = self.merge_fn(a, b)
            x = (x-1) // 2
        a = self.xs[1]
        b = self.xs[2]
        self.xs[0] = self.merge_fn(a, b)

    def getx(self, x):
        """
        get x within 0 <= x < r
        """
        x += (self.size - 1)
        # print("get", x)
        res = self.xs[x]
        x = (x-1) // 2
        while x:
            # print("get", x)
            res += self.xs[x]
            x = (x-1) // 2
        res += self.xs[0] 
        return res

    def query(self, l, r):
        return self._queryrec(l, r, 0, 0, self.size)

    def _queryrec(self, l, r, x, lo, hi):
        if r <= lo or hi <= l:  # no overlap
            return self.default
        elif l <= lo and hi <= r:  # complete overlap
            return self.xs[x]
        else:  # overlap spill
            m = (hi + lo) // 2
            left = self._queryrec(l, r, x*2+1, lo, m)
            right = self._queryrec(l, r, x*2+2, m, hi)
            return self.merge_fn(left, right)

    def update(self, l, r, val):
        self._updaterec(l, r, val, 0, 0, self.size)

    def _updaterec(self, l, r, val, curr, lo, hi):

        if r <= lo or hi <= l:
            return
        elif l <= lo and hi <= r:
            self.xs[curr] = self.merge_fn(self.xs[curr], val)
        else:
            m = (hi + lo) // 2
            self._updaterec(l, r, val, curr*2+1, lo, m)
            self._updaterec(l, r, val, curr*2+2, m, hi)
            # self.xs[curr] = self.merge_fn(self.xs[curr*2+1], self.xs[curr*2+2])


n, q = [int(x) for x in input().split()]
st = ST(n, default=0)
# print(st.xs)

out = []
for _ in range(q):
    arr = [int(x) for x in input().split()]
    # print(arr)
    if arr[0] == 1:
        _, l, r, val = arr
        st.update(l, r, val)
        # print(st.xs)
    else:
        _, pos = arr
        ans = st.getx(pos)
        # print("answer", ans)
        out.append(ans)

out = map(str, out)
print("\n".join(out))
