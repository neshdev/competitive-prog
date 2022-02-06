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

    def update(self, i, x):
        size = self.size
        arr = self.arr 
        y = arr[size+i-1]
        self.setx(i, x+y)

    def update_range(self, lo, hi, x):
        """
        will add +x to A[lo...hi-1]
        will add -x to A[hi]

        What happens for out of bounds?
        Easiest solution is to 2X the size of the array, so you don't have
        to worry about getting out of bounds on the edge cases in powers of 2

        Args:
            lo
            hi
        """
        self.update(lo, x)
        self.update(hi, -x)


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
        k = 0
        for i in range(self.size-1, self.size*2):
            item = (f"val={self.arr[i]},i={k}",)
            out.append(item)
            k += 1
        return out

    def print_tree(self):
        # print(self.arr)
        out = []
        from collections import deque
        q = deque([(0,0)])
        N = self.size
        while q:
            v,l = q.popleft()
            
            if v < 2*N:
                if len(out) < l+1:
                    out.append([])

                val = self.arr[v]
                out[l].append(val)

                
                q.append((v*2+1,l+1))
                q.append((v*2+2,l+1))
        out.pop()
        return out


default = (1,0,0,1)

def merge(r):
    def _merge(a,b):
        a00, a01, a10, a11 = a
        b00, b01, b10, b11 = b

        r00 = ((a00 * b00) % r + (a01 * b10) % r) % r
        r01 = ((a00 * b01) % r + (a01 * b11) % r) % r
        r10 = ((a10 * b00) % r + (a11 * b10) % r) % r
        r11 = ((a10 * b01) % r + (a11 * b11) % r) % r

        return r00, r01, r10, r11
    return _merge

def construct(x):
    return x

def parse_matrix():
    a00, a01 = [int(x) for x in input().split()]
    a10, a11 = [int(x) for x in input().split()]
    return a00, a01, a10, a11

r, n ,m = [int(x) for x in input().split()]
arr = []
for _ in range(n):
    mat = parse_matrix()
    input()
    arr.append(mat)

st = SegmentTree(len(arr), merge(r), default, construct)
st.build(arr)


out = []
for _ in range(m):
    _lo, _hi = [int(x) for x in input().split()]
    _lo -= 1
    a00, a01, a10, a11 = st.query(_lo, _hi)
    ans = f"{a00} {a01}\n{a10} {a11}\n"
    out.append(ans)

print("\n".join(out))