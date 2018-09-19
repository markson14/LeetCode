class Solution:
    """   
        最优子结构是（buy1,sell1,buy2,sell2）
        从头到尾遍历一遍得出最优结果
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1,buy2,sell1,sell2 = -float('inf'), -float('inf'), -float('inf'), -float('inf')
        if not prices: return 0
        for i in prices:
            buy1 = max(buy1,-i)
            sell1 = max(sell1,buy1+i)
            buy2 = max(buy2,sell1-i)
            sell2 = max(sell2,buy2 + i)
        return sell2