#### [763. 划分字母区间](https://leetcode-cn.com/problems/partition-labels/)

难度中等328

字符串 `S` 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

 

**示例 1：**

```
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
```

 

**提示：**

- `S`的长度在`[1, 500]`之间。
- `S`只包含小写字母 `'a'` 到 `'z'` 。
- 

```python
'''
greedy + two pointer
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0]*26
        # 遍历获得字母last index
        for i,v in enumerate(S):
            last[ord(v) - ord('a')] = i
        
        start = end = 0
        res = []
        # 再次遍历
        for i,v in enumerate(S):
          	# 比较当前字母last index大小
            end = max(end, last[ord(v)-ord('a')])
						# 如果当前index等于end，则为一个区间，计算区间长度，start进一
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res
```

