class Solution:
    def dfs(self,x,y,word,i):
        if i == len(word):
            return  True
        
        if 0<=x<len(self.board) and 0<= y < len(self.board[0]) and self.board[x][y] == word[i]:
            temp = self.board[x][y]
            self.board[x][y] = "#"
            # print(word[i],i)
            if self.dfs(x+1,y,word,i+1): return True
            if self.dfs(x-1,y,word,i+1): return True
            if self.dfs(x,y+1,word,i+1): return True
            if self.dfs(x,y-1,word,i+1): return True
            self.board[x][y] = temp
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.count = 0
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i,j,word,0):
                        return True
        return False