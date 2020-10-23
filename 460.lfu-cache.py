#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from collections import defaultdict, OrderedDict, Counter
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(OrderedDict)
        self.key_freq = Counter()
        self.min_freq = 1
        
    def update(self, key:int, value=None):
        freq = self.key_freq[key]
        nxt_freq = freq + 1
        self.key_freq[key] = nxt_freq
        res = self.cache[freq].pop(key)
        if not self.cache[freq] and freq == self.min_freq:
            self.min_freq = nxt_freq
        self.cache[nxt_freq][key] = res if not value else value
        return res
        

    def get(self, key: int) -> int:
        
        if key in self.key_freq:
            res = self.update(key)
            # print('get', self.cache, self.key_freq)
            return res
        else:
            # print('get', self.cache, self.key_freq)
            return -1


    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key_freq:
            self.update(key, value) 
        else:
            if len(self.key_freq) >= self.cap:
                self.key_freq.pop(self.cache[self.min_freq].popitem(last=False)[0])
            self.min_freq = 1
            self.key_freq[key] = 1
            self.cache[1][key] = value
        # print('put', self.cache, self.key_freq)

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

