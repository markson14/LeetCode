class Solution:
    
    def equals(self,s,t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and self.equals(s.left,t.left) and self.equals(s.right,t.right)
    
    def traverse(self,s,t):
        return s != None and (self.equals(s,t) or self.traverse(s.left,t) or self.traverse(s.right,t))
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traverse(s,t)