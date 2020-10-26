#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusone(cur, i):
            if cur[i] == '9':
                return cur[:i]+'0'+cur[i+1:]
            else:
                return cur[:i]+str(int(cur[i])+1)+cur[i+1:]
        def minusone(cur, i):
            if cur[i] == '0':
                return cur[:i]+'9'+cur[i+1:]
            else:
                return cur[:i]+str(int(cur[i])-1)+cur[i+1:]

        q = deque()
        q.append('0000')
        visited = set('0000')
        step = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                for i in range(4):
                    up = plusone(cur, i)
                    down = minusone(cur, i)
                    if not up in visited:
                        q.append(up)
                        visited.add(up)
                    if not down in visited:
                        q.append(down)
                        visited.add(down)
            step += 1

        return -1
# @lc code=end

