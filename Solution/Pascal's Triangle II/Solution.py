class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1,rowIndex+1):
            n = i+1
            tmp = [1 for _ in range(n)]
            tmpp = res
            for j in range(1,len(tmp)-1):
                tmp[j] = tmpp[j-1] + tmpp[j]
            res = tmp
        return res