#### [56. Merge Intervals](https://leetcode-cn.com/problems/merge-intervals/)

难度中等662

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

**Constraints:**

- `intervals[i][0] <= intervals[i][1]`



```python
'''
sort on key
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      	# 对初始index进行排序
        intervals.sort(key=lambda x:x[0])
        merge = []
        for inter in intervals:
          	# 如果merge为空或者merge.top[1]小于inter[0]，则可以把当前inter添加进merge
            if not merge or merge[-1][1] < inter[0]:
                merge.append(inter)
            # 比较当前inter[1]和merge.top[1]的大小，将其更新为两者最大值
            else:
                merge[-1][1] = max(merge[-1][1], inter[1])
        
        return merge
```

