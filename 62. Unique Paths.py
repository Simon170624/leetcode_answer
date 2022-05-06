# 1. math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        if m > n:
            m, n = n, m

        temp = 1
        res = 1
        for i in range(1, m):
            temp *= i
        for i in range(n, m + n - 1):
            res *= i
        return res // temp
# dynamic programming
class Solution:
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]