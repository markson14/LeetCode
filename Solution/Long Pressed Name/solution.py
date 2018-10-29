import itertools
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        g1 = [[k,len(list(v))] for k,v in itertools.groupby(name)]
        g2 = [[k,len(list(v))] for k,v in itertools.groupby(typed)]
        
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1,v1),(k2,v2) in zip(g1,g2))