import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        group, rest = max(collections.Counter(collections.Counter(tasks).values()).items())
        return max(len(tasks), (group-1)*(n+1)+rest)
        