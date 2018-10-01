class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        res = [[1]]
        for i in range(1,numRows):
            n = i+1
            tmp = [1 for _ in range(n)]
            tmpp = res[-1]
            for j in range(1,len(tmp)-1):
                tmp[j] = tmpp[j-1] + tmpp[j]
            res.append(tmp)
        return res