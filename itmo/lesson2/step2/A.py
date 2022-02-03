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


n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
NEG_INF = float('-inf')
default = (0,0,0,0)

def merge(a,b):
    seg1, suf1, pref1, total1 = a
    seg2, suf2, pref2, total2 = b
    seg = max(
        seg1,
        seg2,
        suf1+pref2
    )
    suf = max(
        suf2,
        total2 + suf1
    )
    pref = max(
        pref1,
        total1 + pref2
    )
    total = total1 + total2
    return seg, suf, pref, total

def construct(x):
    if x > 0:
        return (x,x,x,x)
    else:
        return (0,0,0,x)

def max_segment(st: SegmentTree):
    seg, pre, suf, total = st.query(0, st.size)
    return seg

st = SegmentTree(n, merge, default, construct)
st.build(arr)

ans = [max_segment(st)]
for _ in range(m):
    query = [int(x) for x in input().split()]
    i, v = query
    st.setx(i,v)
    ans.append(max_segment(st))

ans = map(str, ans)
# print(ans)
print("\n".join(ans))