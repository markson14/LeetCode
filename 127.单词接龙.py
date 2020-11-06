#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def one_diff(x, y):
            # if len(x) != len(y): return False
            tag = 0
            for i in range(len(x)):
                if x[i] == y[i]:
                    continue
                tag += 1
            return tag == 1

        queue = []
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        step = 1  # 记录扩散的步数
        while queue:
            sz = len(queue)
            # 将当前队列中的所有节点向四周扩散
            step += 1
            for i in range(sz):
                cur = queue.pop()
                # 划重点：这里判断是否到达终点
                if cur == endWord:
                    return step
                # 将 cur 的相邻节点加入队列, adj()为cur上下左右的点
                for x in wordList:
                    if x not in visited and one_diff(cur, x):
                        queue.append(x)
                        visited.add(x)
            # 划重点：更新步数在这里
        return 0

        
# @lc code=end
