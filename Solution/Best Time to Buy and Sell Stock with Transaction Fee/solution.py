class Solution:
    """
        画出流程图，建立array储存
        难度：Medium
    """
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        days = len(prices)
        if not prices or days <= 1: return 0
        buy,h1,sell,h2 = [None]*days,[None]*days,[None]*days,[None]*days
        buy[0] = h1[0] = -prices[0]
        sell[0] = h2[0] = 0
        for i in range(1,days):
            buy[i] = max(h2[i-1],sell[i-1]) - prices[i]
            h1[i] = max(h1[i-1],buy[i-1])
            sell[i] = max(buy[i-1],h1[i-1]) + prices[i] - fee
            h2[i] = max(h2[i-1],sell[i-1])
        return max(sell[days-1], h2[days-1])
            