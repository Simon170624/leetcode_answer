class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new = list(range(len(nums) + 1))
        
        return sum(new) - sum(nums)