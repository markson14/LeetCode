class Solution:
"""
    完全背包问题：因为物品可以无限制使用，列表找关系式。
    如果用min判断则会超时，所以用if else判断大小
    难度：Medium
"""
     def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [0] + [float('inf')]*amount
        for i in range(1,amount+1):
            for coin in coins:
                # 防止超时，所以用if else 判断
                if i >= coin:
                    if dp[i] >= dp[i-coin]+1:
                        dp[i] = dp[i-coin]+1
                    else:
                        dp[i] = dp[i]
        return dp[-1] if not dp[amount] > amount else -1
        