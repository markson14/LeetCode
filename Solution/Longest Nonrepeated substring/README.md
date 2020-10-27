# Longest Substring without repeating characters

Given a string, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
```

**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```



```python
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = defaultdict(int)
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            c1 = s[right]
            right += 1
            windows[c1] += 1
            
            if right - left == len(windows):
                max_len = max(max_len, right-left)
            
            # print(left, right, s[left:right], max_len)
            
            while windows[c1] > 1:
                c2 = s[left]
                left += 1
                windows[c2] -= 1
                if windows[c2] == 0:
                    del windows[c2]
                
        return max_len
```

