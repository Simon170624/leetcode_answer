class Solution:
    def helper(self, board, x, y, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        if board[x][y] != 'O':
            return 
        board[x][y] = 'Y'
        self.helper(board, x - 1, y, m, n)
        self.helper(board, x, y - 1, m, n)
        self.helper(board, x + 1, y, m, n)
        self.helper(board, x, y + 1, m, n)
    
    def is_border(self, board, x, y, m, n):
        if x == 0 or y == 0 or x == m - 1 or y == n - 1:
            return True
        return False
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                if self.is_border(board, x, y, m, n) == False:
                    continue
                if board[x][y] == 'O':
                    self.helper(board, x, y, m, n)
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                if board[x][y] == 'Y':
                    board[x][y] = 'O'