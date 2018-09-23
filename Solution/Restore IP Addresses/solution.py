class Solution:
"""
    层层判断，判断条件为：
                    部分大于255或着部分的开头不为零
                满足条件的都添加进res
"""
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or n > 12:
            return []
        res = []
        for a in range(1, n-2):
            if int(s[0:a]) > 255 or s[0:a] != str(int(s[0:a])): 
                continue
            for b in range(a+1,n-1):
                if int(s[a:b]) > 255 or s[a:b] != str(int(s[a:b])): 
                    continue
                for c in range(b+1,n):
                    if int(s[b:c]) > 255 or s[b:c] != str(int(s[b:c])): 
                        continue
                    if int(s[c:]) > 255 or s[c:] != str(int(s[c:])): 
                        continue
                    res.append(s[0:a]+'.'+s[a:b]+'.'+s[b:c]+'.'+s[c:])
        return resol