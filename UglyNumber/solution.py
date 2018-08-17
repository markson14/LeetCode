class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        res=[2**i*3**j*5**k  for i in range(30)  for j in range(20)   for k in range(15)]
        res.sort()
        return res[index-1] if index else 0