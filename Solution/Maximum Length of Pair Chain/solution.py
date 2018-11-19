class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        """
            Interval Problem, greedy, sorted by the ending points 
        """

        pairs = sorted(pairs, key = lambda x:x[1])
        count,cur = 0,float('-inf')
        for x,y in pairs:
            if cur < x:
                cur = y
                count += 1
        return count 