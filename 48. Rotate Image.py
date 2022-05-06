class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
                l += 1
                r -= 1