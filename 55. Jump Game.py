# recursion can be used, but no enough space
# 1. O(n^2), too slow but this is the DP template
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        
        for i in range(1, n):
            for j in range(i):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break
        
        return dp[n - 1]
#2. O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        dp = 0
        
        for i in range(n - 1):
            dp = max(dp, i + nums[i])
            if dp == i:
                return False
        
        return True