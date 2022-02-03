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
default = 0

def merge(a,b):
    return a + b

def construct(x):
    return x

def kth_one(st: SegmentTree, k):
    N = st.size * 2
    q = [(0,0,st.size,k)]
    while q:
        i,lo,hi,k = q.pop()
        if hi - lo == 1:
            return lo
        m = (lo + hi) // 2

        if i*2 + 1 < N:
            s = st.arr[i*2+1]
            if k < s:
                q.append((i*2+1, lo, m, k ))
            else:
                q.append((i*2+2, m, hi, k - s ))
    return 0


st = SegmentTree(n, merge, default, construct)
st.build(arr)
ans = []
for _ in range(m):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        _, i = query
        idx = st.size + i - 1
        # print("idx", idx)
        val = 0 if st.arr[idx] else 1
        st.setx(i,val)
    else:
        _, k = query
        ans.append (kth_one(st, k))

ans = map(str, ans)
print("\n".join(ans))
