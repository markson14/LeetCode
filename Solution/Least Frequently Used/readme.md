- #### [460. LFU Cache](https://leetcode-cn.com/problems/lfu-cache/)

  Design and implement a data structure for [Least Frequently Used (LFU)](https://en.wikipedia.org/wiki/Least_frequently_used) cache.

  Implement the `LFUCache` class:

  - `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
  - `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
  - `void put(int key, int value)` Sets or inserts the value if the `key` is not already present. When the cache reaches its `capacity`, it should invalidate the least frequently used item before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), **the least recently** used `key` would be evicted.

  **Notice that** the number of times an item is used is the number of calls to the `get` and `put` functions for that item since it was inserted. This number is set to zero when the item is removed.

  **Follow up:**
  Could you do both operations in **O(1)** time complexity?

   

  **Example 1:**

  ```
  Input
  ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
  [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
  Output
  [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
  
  Explanation
  LFUCache lFUCache = new LFUCache(2);
  lFUCache.put(1, 1);
  lFUCache.put(2, 2);
  lFUCache.get(1);      // return 1
  lFUCache.put(3, 3);   // evicts key 2
  lFUCache.get(2);      // return -1 (not found)
  lFUCache.get(3);      // return 3
  lFUCache.put(4, 4);   // evicts key 1.
  lFUCache.get(1);      // return -1 (not found)
  lFUCache.get(3);      // return 3
  lFUCache.get(4);      // return 4
  ```

   

  **Constraints:**

  - `0 <= capacity, key, value <= 104`
  - At most `105` calls will be made to `get` and `put`.



```python
from collections import defaultdict, OrderedDict, Counter
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(OrderedDict)
        self.key_freq = Counter()
        self.min_freq = 1
        
    def update(self, key:int, value=None):
      	'''
      	update cache status if key in cache already. 
      		- data_freq += 1
      		- cache[freq] += 1, cache[freq][key] = value
      	'''
        freq = self.key_freq[key]
        nxt_freq = freq + 1
        self.key_freq[key] = nxt_freq
        res = self.cache[freq].pop(key)
        if not self.cache[freq] and freq == self.min_freq:
            self.min_freq = nxt_freq
        self.cache[nxt_freq][key] = res if not value else value
        return res
        

    def get(self, key: int) -> int:
      	'''
      	if key in cache, update status, else return -1
      	'''
        if key in self.key_freq:
            res = self.update(key)
            # print('get', self.cache, self.key_freq)
            return res
        else:
            # print('get', self.cache, self.key_freq)
            return -1


    def put(self, key: int, value: int) -> None:
      	# edge case cap == 0
        if self.cap == 0:
            return
        # update value if key in key_freq
        if key in self.key_freq:
            self.update(key, value) 
        else:
          	# len >= cap, do remove least frequently used element
            if len(self.key_freq) >= self.cap:
                self.key_freq.pop(self.cache[self.min_freq].popitem(last=False)[0])
            # add new element to cache and key_freq
            self.min_freq = 1
            self.key_freq[key] = 1
            self.cache[1][key] = value
        # print('put', self.cache, self.key_freq)
```

