# Minimum Window Substring

------

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

**Example:**

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

**Note:**

- If there is no such window in S that covers all characters in T, return the empty string `""`.
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

  

```python
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        windows = defaultdict(int)
        for c in t: need[c] += 1
        left, right = 0,0
        match = 0
        min_len = float('INF')
        res = ''
        while right < len(s):
            c = s[right]
            # 如果需要c，将c移入窗口
            if c in need:
                windows[c] += 1
                # 是否match
                if windows[c] == need[c]:
                    match += 1
            # 右指针右移
            right += 1
            # 当match达到要求，收缩左指针
            while match == len(need):
                # 判断是否为最小sub
                if right - left < min_len:
                    min_len = right-left
                    res = s[left:right]
                c2 = s[left]
                # 移除左指针出窗口
                if c2 in need:
                    windows[c2] -= 1
                    if windows[c2] < need[c2]:
                        match -= 1
                left += 1
        
        return res
```

