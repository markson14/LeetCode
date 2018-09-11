
class Solution(object): #1Union Find 
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """    
        def find(x):
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]
        
        if not M: return 0
        n = len(M)
        f = [i for i in range(n)]
        for i in range(n):
            for j in range(i,n):
                if M[i][j]:
                    iid = find(i)
                    jid = find(j)
                    if iid != jid:
                        f[iid] = jid
        c = 0
        for i in range(n):
            if f[i] == i:
                c+=1
        return c

class Solution(object):  # DFS
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        people = [0] * len(M)
        circles = 0
        for i in range(len(M)):
            if people[i] == 0:
                self.dfs(M, people, i)
                circles += 1            
        return circles
    
    def dfs(self, M, people, i):
        for j in range(len(M)):
            if M[i][j] == 1 and people[j] == 0:
                people[j] = 1
                self.dfs(M, people, j)