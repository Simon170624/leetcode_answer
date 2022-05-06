# ls[:] rather than ls
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        if not nums:
            return self.res
        
        self.length = len(nums)
        self.helper(nums, [], 0)
        return self.res
    
    def helper(self, nums, ls, index):
        if index == self.length:
            self.res.append(ls[:])
            return
        
        for num in nums:
            if num in ls:
                continue
            else:
                ls.append(num)
                self.helper(nums, ls, index + 1)
                ls.pop()
        return 