

#### [239. Sliding Window Maximum](https://leetcode-cn.com/problems/sliding-window-maximum/)

难度困难598

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

 

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Example 3:**

```
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

**Example 4:**

```
Input: nums = [9,11], k = 2
Output: [11]
```

**Example 5:**

```
Input: nums = [4,-2], k = 2
Output: [4]
```

 

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `1 <= k <= nums.length`



```python
from collections import deque

class MonotonicQueue(deque):
        def push_back(self, n):
            while self and self[-1] < n:
                self.pop()
            self.append(n)

        def max(self):
            return self[0]
        
        def pop_n(self, n):
            if self and self[0] == n:
                self.popleft()
        
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []
        for i in range(len(nums)):
            if i < k-1:
                window.push_back(nums[i])
            else:
                window.push_back(nums[i])
                res.append(window.max())
                window.pop_n(nums[i-k+1])
            
        return res
```

