#### [438. Find All Anagrams in a String](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

难度中等395

Given a string **s** and a **non-empty** string **p**, find all the start indices of **p**'s anagrams in **s**.

Strings consists of lowercase English letters only and the length of both strings **s** and **p** will not be larger than 20,100.

The order of output does not matter.

**Example 1:**

```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```



**Example 2:**

```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```





```python
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windows, need = defaultdict(int), defaultdict(int)
        for c in p: need[c]+=1
        left, right = 0,0
        match = 0
        res = []
        while right < len(s):
            c1 = s[right]
            right += 1
            if c1 in need:
                windows[c1] += 1
                if windows[c1] == need[c1]:
                    match += 1
            
            # print(left, right, s[left:right])
            while match == len(need):
                if right - left == len(p):
                    res.append(left)
                c2 = s[left]
                left += 1
                if c2 in need:
                    if windows[c2] == need[c2]:
                        match -= 1
                    windows[c2] -= 1
        return res
```

