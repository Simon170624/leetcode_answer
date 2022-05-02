class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        nums = list(nums)
        nums = sorted(nums)
        res = 1
        p = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                res = max(res, i - p + 1)
            else:
                p = i
        
        return res