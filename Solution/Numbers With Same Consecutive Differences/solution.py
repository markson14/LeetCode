class Solution1:
    
    def dp(self,cur,res,index,N,K):
        if N == 0:
            res.append(cur)
        
        elif not cur:
            for i in range(1,10):
                if i+K < 10 or i-K>=0:
                    self.dp(str(i),res,index+1,N-1,K)
        else:
            right = int(cur[index]) + K
            left = int(cur[index]) - K
            tmp1 = tmp2 = cur
            if right < 10:
                tmp1 += str(right)
                self.dp(tmp1,res,index+1,N-1,K)
            if left >= 0:
                tmp2+=str(left)
                self.dp(tmp2,res,index+1,N-1,K)
            
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [_ for _ in range(10)]
        if K==0 and N == 1:
            res = [0]
        else:
            res = []
        self.dp("",res,-1,N,K)
        res = list(set(res))
        res = list(map(int,res))
        return res


class Solution2(object):
    def numsSameConsecDiff(self, N, K):
        ans = {x for x in range(1, 10)}
        for _ in range(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)