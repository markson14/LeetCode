# -*- coding:utf-8 -*-
# 循环法求斐波那契数列，每次保存上一次结果，避免重复计算
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        result_list = []
        a, b = 0, 1
        while n > 0:
            result_list.append(b)
            a, b = b, a + b
            n -= 1
        return result_list[-1]