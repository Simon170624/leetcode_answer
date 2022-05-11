# recursion
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = {}
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                visited[i * m + j] = False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i * m + j] = True
                    tmp = self.dfs(board, word, 0, i, j, n, m, visited)
                    visited[i * m + j] = False
                    if tmp == True:
                        return True
        return False
    
    def dfs(self, board, word, now, x, y, n, m, visited):
        zx = [0, 0, 1, -1]
        zy = [1, -1, 0, 0]

        if now == len(word) - 1:
            return True
        
        for i in range(4):
            nx = x + zx[i]
            ny = y + zy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != word[now + 1] or visited[nx * m + ny] == True:
                continue
            
            visited[nx * m + ny] = True
            tmp = self.dfs(board, word, now + 1, nx, ny, n, m, visited)
            
            visited[nx * m + ny] = False
            if tmp == True:
                return True
        return False