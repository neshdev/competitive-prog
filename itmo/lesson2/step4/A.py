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


default = 0

def merge(a,b):
    return a+b

def construct(x):
    return x


N = int(input())

arr = [int(x) for x in input().split()]

st0 = SegmentTree(N, merge, default, construct)
st1 = SegmentTree(N, merge, default, construct)

arr1 = [x if i % 2 == 0 else -x for i,x in  enumerate(arr)]
arr2 = [-x if i % 2 == 0 else x for i,x in  enumerate(arr)]

st0.build(arr1)
st1.build(arr2)

M = int(input())

ans = []
for _ in range(M):
    query = [int(x) for x in input().split()]
    # print(query)
    if query[0] == 1:
        _, _lo, _hi = query
        
        if (_lo-1) % 2 == 0:
            val = st0.query(_lo-1, _hi)
            ans.append(val)
        else:
            val = st1.query(_lo-1, _hi)
            ans.append(val)
    else:
        _, i, j = query
        if i % 2 == 0:
            st0.setx(i-1, -j)
            st1.setx(i-1, j)
        else:
            st0.setx(i-1, j)
            st1.setx(i-1, -j)
        
ans = map(str, ans)
print("\n".join(ans))
# # # for x in st.print_tree():
# # #     print(x)

# import random

# N = 100
# MAX_INT = 100
# T = 100
# arr = []
# for i in range(N):
#     arr.append(random.randint(0,MAX_INT))

# arr1 = [x if i % 2 == 0 else -x for i,x in  enumerate(arr)]
# arr2 = [-x if i % 2 == 0 else x for i,x in  enumerate(arr)]

# st0 = SegmentTree(N, merge, default, construct)
# st1 = SegmentTree(N, merge, default, construct)

# st0.build(arr1)
# st1.build(arr2)


# for i in range(T):
#     lo = random.randint(0, N-1)
#     hi = random.randint(lo, N-1)

#     sign = 1
#     total = 0
#     # print(lo, hi)
#     for i in range(lo, hi+1):
#         total += arr[i] * sign
#         sign = sign*-1
#     if lo % 2 == 0:
#         ans = st0.query(lo,hi+1)
#     else:
#         ans = st1.query(lo,hi+1)
#     if ans == total:
#         print(ans == total, ans, total)
#     else:
#         raise Exception("Error", arr, total, ans)