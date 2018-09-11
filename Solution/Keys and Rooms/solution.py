"""
    dfs先遍历每一个rooms里的room，若没有访问过，添加进set里。若访问过
    return退出。最后返回判断set长度是否与rooms长度相等即可
"""
class Solution(object):
    
    def dfs(self,room,rooms):
        if room in self.visited:
            return
        self.visited.add(room)
        for key in rooms[room]:
            self.dfs(key,rooms)
        
    
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.visited = set()
        self.dfs(0,rooms)
        return len(self.visited) == len(rooms)