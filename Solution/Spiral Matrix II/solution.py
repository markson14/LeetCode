class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def spiral(c1,c2,r1,r2):
            for c in range(c1,c2+1):
                yield r1, c
            for r in range(r1+1,r2+1):
                yield r,c2
            if c2>c1 and r2>r1:
                for c in range(c2-1,c1,-1):
                    yield r2,c
                for r in range(r2,r1,-1):
                    yield r,c1
        matrix = [[0]*n for _ in range(n)]
        start = 1
        c1,c2 = 0,n-1
        r1,r2 = 0,n-1
        while c1 <= c2 and r1 <= r2:
            for r,c in spiral(c1,c2,r1,r2):
                # print(r,c)
                matrix[r][c] = start
                start += 1
            c1 += 1; c2-=1 ;r1+=1;r2-=1
        return matrix