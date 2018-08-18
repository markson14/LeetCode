class Solution(object):
    def dfs(self,x,y,pad):
        if x<0 or y<0 or x>len(pad)-1 or y>len(pad[0])-1 or pad[x][y] != 'O':
            return None
        pad[x][y] = '#'
        self.dfs(x-1,y,pad)
        self.dfs(x,y-1,pad)
        self.dfs(x+1,y,pad)
        self.dfs(x,y+1,pad)
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) > 0:
            m,n = 0,0
            for n in range(len(board[0])):
                if board[m][n] == 'O':
                    self.dfs(m,n,board)
            for m in range(1,len(board)):
                if board[m][n] == 'O':
                    self.dfs(m,n,board)
            for n in range(len(board[0])-1,-1,-1):
                if board[m][n] == 'O':
                    self.dfs(m,n,board)
            for m in range(len(board)-1,0,-1):
                if board[m][n] == 'O':
                    self.dfs(m,n,board)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '#':
                        board[i][j] = 'O'
                    else:
                        board[i][j] = 'X'
                
            