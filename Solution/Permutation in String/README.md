# Permutation in String

Given two strings s1 and s2, write a function to return true if s2

contains the permutation of  s1. In other words, one of the first string's permutations is the substring of the second string.

**Example 1:**

```
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
```



**Example 2:**

```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```



**Note:**

1. The input strings only contain lower case letters.
2. The length of both given strings is in range [1, 10,000].



```python
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        windows = defaultdict(int)
        match = 0
        left, right = 0,0
        for c in s1: need[c] += 1
        while right < len(s2):
            c1 = s2[right]
            right += 1
            # 拓展右边界
            if c1 in need:
                windows[c1] += 1
                if windows[c1] == need[c1]:
                    match += 1
            # 如果长度大于s1，开始收缩
            while right - left >= len(s1):
                # 判断是否可以return
                if match == len(need):
                    return True
                # 收缩左边界
                c2 = s2[left]
                left += 1
                if c2 in need:
                    if windows[c2] == need[c2]:
                        match -= 1
                    windows[c2] -= 1                
            
        return False
```


