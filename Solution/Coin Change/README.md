# Coin Change

You are given coins of different denominations and a total amount of money *amount*. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

**Example 1:**

```
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```



```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      	# 初始化dp，值为amount+1，方便后续min操作
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
              	# 子状态小于0，则继续
                if i-coin < 0: continue
                # 反之，则比较当前和使用当前coin的最小值
                else:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # 如果最后一个不等于初始化的amount+1，则return，反之return -1
        return dp[amount] if dp[amount] != amount+1 else -1
```

