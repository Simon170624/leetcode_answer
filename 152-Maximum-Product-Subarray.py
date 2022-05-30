# dp
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_curr = min_curr = nums[0]
        
        for i in range(1, len(nums)):
            tmp = min_curr
            min_curr = min(nums[i], tmp * nums[i], max_curr * nums[i])
            max_curr = max(nums[i], tmp * nums[i], max_curr * nums[i]) 
            dp[i] = max(min_curr, max_curr)
        
        return max(dp)