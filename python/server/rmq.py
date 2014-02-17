
class RangeQuery():
    """
        This class implements the Range (Minimum / Maximum) Query. Min / Max is decided based on the Comparator
        Build time is O(n log n), Query time is O(log n)

    """
    def __init__(self,items,comparator, default):
        arr_size = len(items)
        self.comparator = comparator
        self.default = default
        self.n = arr_size
        self.__B(items, arr_size)

    def __lch(self,node):
        return (node << 1) + 1;

    def __rch(self,node):
        return self.__lch(node) + 1;

    def __mid(self, b, e):
        return b + ((e - b) // 2)

    def __parent(node):
        return node >> 1

    def __log2(self,num):
        base = 2
        exp = 0
        init = 1
        while(init < num):
            init *= base
            exp += 1
        return exp

    def __pow(self,n, r):
        if r == 0:
            return 1
        elif r == 1:
            return n
        elif r % 2 == 0:
            x = self.__pow(n, r / 2)
            return x * x
        else:
            x = self.__pow(n, r / 2)
            return n * x * x

    def __build(self,A,start, end,M, node):
        if start == end:
            M[node] = A[start]
            return A[start]

        else:
            mid = self.__mid(start, end)
            x1 = self.__build(A,start, mid, M, self.__lch(node))
            x2 = self.__build(A, mid + 1, end, M,self.__rch(node))
            M[node] = self.comparator(x1, x2)
            return M[node]

    def __B(self, A, n):
        RM_h = self.__log2(n)
        RM_MSize = 2 * self.__pow(2, RM_h)  - 1
        M = [self.default for i in xrange(0, RM_MSize)]
        self.__build(A, 0, n - 1, M, 0)
        self.M = M

    def __query(self, start, end, qstart, qend, index):
        if (qstart <= start) and (qend >= end):
            return self.M[index]
        if (end < qstart) or (start > qend):
            return self.default
        mid = self.__mid(start, end)
        x1 = self.__query(start, mid, qstart, qend, self.__lch(index))
        x2 = self.__query(mid + 1, end, qstart, qend, self.__rch(index))
        ans =  self.comparator(x1, x2)
        return ans

    def query(self, qstart, qend):
        return self.__query(0, self.n - 1, qstart, qend, 0)