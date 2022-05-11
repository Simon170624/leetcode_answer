# brust force O(mn) 229ms list.append
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        positions = []
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            if 0 not in matrix[r]:
                continue
            else:
                for l in range(n):
                    if matrix[r][l] == 0:
                        positions.append([r, l])
        
        for position in positions:
            r = position[0]
            l = position[1]
            for col in range(n):
                matrix[r][col] = 0
            for row in range(m):
                matrix[row][l] = 0

# create row list and col list, assign is better than append
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix)==0:
            return
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# 