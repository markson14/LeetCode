class Solution:
    """
        难度：Medium
        动态规划
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return(0)
        sell, buy, pre_sell, pre_buy = 0, -prices[0], 0, 0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)
        return(max(buy, sell))

class Solution:
    """
        画流程图
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if not prices or days <= 1: return 0
        buy,h1,sell,h2 = [None]*days,[None]*days,[None]*days,[None]*days
        buy[0] = h1[0] = -prices[0]
        sell[0] = h2[0] = 0
        for i in range(1,days):
            buy[i] = h2[i-1] - prices[i]
            h1[i] = max(buy[i-1],h1[i-1])
            sell[i] = max(buy[i-1],h1[i-1])+prices[i]
            h2[i] = max(h2[i-1],sell[i-1])
            
        return max(sell[days-1],h2[days-1])
    