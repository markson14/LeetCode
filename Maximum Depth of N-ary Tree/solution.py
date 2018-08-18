class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        if not root.children: return 1
        
        depth = 0
        q = [root, 'X']
        while q:
            node = q.pop(0)
            if node == 'X':
                depth += 1
                if q: 
                    q.append('X')
                continue
            else:
                for c in node.children:
                    q.append(c)
        return depth
                
        