class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return []
        
        return self.helper(nums)
    
    def helper(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])
        root.left = self.helper(nums[0 : mid])
        root.right = self.helper(nums[mid + 1 : len(nums)])
        
        return root