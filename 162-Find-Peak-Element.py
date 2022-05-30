# O(logn) - Binary Search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[1] > nums[0] else 0
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else: # nums[mid] > nums[mid - 1] & > nums[mid + 1]
                return mid

        if nums[start] < nums[end]:
            return end
        else:
            return start