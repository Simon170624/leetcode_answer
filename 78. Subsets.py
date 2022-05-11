# Time Limit Exceeded	
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        self.length = len(nums)
        self.nums = nums
        self.res = []
        for n in range(1, len(nums) + 1):
            self.helper(n, 0, [])
        self.res.append([])
        return self.res
        
    def helper(self, n, index, curr):
        if index == n:
            curr = sorted(curr)
            if curr not in self.res:
                self.res.append(curr[:])
            return
        
        for num in self.nums:
            if num not in curr:
                curr.append(num)
                self.helper(n, index + 1, curr)
                curr.pop()

# range(index, len(nums)); have checked the elements before index
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums = sorted(nums)
        res = []
        self.helper(nums, 0, [], res)
        return res
        
    def helper(self, nums, index, curr, res):
        res.append(curr[:])
        
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.helper(nums, i + 1, curr, res)
            curr.pop()