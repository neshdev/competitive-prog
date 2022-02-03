from calendar import c
from operator import gt
import sys

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

class SegmentTree:
    def __init__(self, n, f=lambda x,y: x+y, default=0, construct=lambda x: x):
        size = 1
        while size < n:
            size *= 2
        self.arr = [default] * (2*size)
        self.size = size
        self.default = default
        self.f = f
        self.construct = construct

    def build(self, xs):
        N = len(xs)
        for i in range(N):
            self.arr[self.size + i - 1] = self.construct(xs[i])

        for i in range(self.size-2,-1,-1):
            # print(i)
            left = self.arr[i*2+1]
            right = self.arr[i*2+2]
            self.arr[i] = self.f(left,right)



    def __setx(self, i, x, curr, lo, hi):
        # print(f"{hi=},{lo=},{curr=},{i=},{x=}")
        if (hi - lo) == 1:
            self.arr[curr] = self.construct(x)
            return
        m = (lo + hi) // 2
       
        if i < m:
            self.__setx(i,x,curr*2+1,lo, m)
        else:
            self.__setx(i,x,curr*2+2,m, hi)
        
        left = self.arr[curr*2+1]
        right = self.arr[curr*2+2]
        self.arr[curr] = self.f(left, right)


    def setx(self, i , x):
        self.__setx(i,x,0,0,self.size)

    def __query(self, l, r, curr, lox, hix):
        # print(f"{l=},{r=},{curr=},{lox=},{hix=}")
        """
        3 cases:
        1)   
                        lox-------hix l----------r
           l----------r lox-------hix
        2)   l--------------------------r
                    lox-------hix
        3)          lo----------hi   
                            lox-------hix
                    lo----------hi   
                lox-------hix
                    
        """
        if lox >= r or l >= hix:
            return self.default
        elif lox >= l and hix <= r:
            return self.arr[curr]
        else:
            m = (lox + hix) // 2
            left = self.__query(l, r, curr*2+1, lox, m)
            right = self.__query(l, r, curr*2+2, m, hix)
            return self.f(left, right)
        

    def query(self, lo, hi):
        res = self.__query(lo, hi, 0, 0, self.size)
        return res

    def print(self):
        out = []
        for i in range(self.size, self.size*2):
            item = (f"val={self.arr[i]},i={i - self.size}",)
            out.append(item)
        return out



default = 0

def merge(a,b):
    return a + b

def construct(x):
    return x

def gt_than_rec(st: SegmentTree, x, curr, lo, hi):
    # print(x, curr, lo, hi, (hi+lo) // 2)
    if st.arr[curr] <= x:
        return -1
    if hi - lo == 1:
        return lo
    m = (hi + lo) // 2
    res = gt_than_rec(st, x, curr*2+1, lo, m)
    if res == -1:
        # print("going right")
        res = gt_than_rec(st, x - st.arr[curr*2+1], curr*2+2, m, hi)
    return res


def gt_than(st: SegmentTree, x):
    return gt_than_rec(st, x, 0, 0, st.size)

N = int(input())
gts = [int(x) for x in input().split()]
arr = [1]*N
st = SegmentTree(N, merge, default, construct)
st.build(arr)
xs = []
for i in range(N-1,-1,-1):
    x = gts[i]
    ans = gt_than(st, x)
    st.setx(ans,0)
    # print(ans, end=" ")
    xs.append(N-ans)

for i in range(N-1,-1,-1):
    print(xs[i], end=" ")
