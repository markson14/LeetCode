# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x:x.end)
        last = intervals[0]
        count = 0
        for i in intervals[1:]:
            if i.start < last.end:
                count += 1
            else:
                last = i
        return count