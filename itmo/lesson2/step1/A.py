class SegmentTree:
    def __init__(self, n, f=lambda x,y: x+y, default=0):
        size = 1
        while size < n:
            size *= 2
        self.arr = [default] * (2*size)
        self.size = size
        self.default = default
        self.f = f

    # def build(self, xs):
    #     N = len(xs)
    #     for i in range(N):
    #         # print(self.size + i - 1)
    #         self.arr[self.size + i - 1] = xs[i]

    #     for i in range(self.size-2,-1,-1):
    #         # print(i)
    #         left = self.arr[i*2+1]
    #         right = self.arr[i*2+2]
    #         self.arr[i] = self.f(left,right)

    def build(self, xs):
        self.__build(xs, 0, 0, self.size)

    def __build(self, xs, curr, lo, hi):
        if hi - lo == 1:
            if (lo < len(xs)):
                self.arr[curr] = xs[lo]
        else:
            m = (lo + hi) // 2
            self.__build(xs, curr*2+1, lo, m)
            self.__build(xs, curr*2+2, m, hi)

            left = self.arr[curr*2+1]
            right = self.arr[curr*2+2]
            self.arr[curr] = self.f(left, right)



    def __setx(self, i, x, curr, lo, hi):
        # print(f"{hi=},{lo=},{curr=},{i=},{x=}")
        if (hi - lo) == 1:
            self.arr[curr] = x
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
st = SegmentTree(n)
st.build(arr)

for _ in range(m):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        _, i, v = query
        st.setx(i,v)
        
    else:
        _, _lo, _hi = query
        out = st.query(_lo, _hi)
        print(out)