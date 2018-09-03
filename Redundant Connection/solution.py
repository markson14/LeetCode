class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        def find(l,x):
            while l[x] != x:
                x = l[x]
            return x
        l = [i for i in range(n+1)]
        for u,v in edges:
            u_f = find(l,u)
            v_f = find(l,v)
            if u_f != v_f:
                l[v_f] = u_f
            else:
                return[u,v]