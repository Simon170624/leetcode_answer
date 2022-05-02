# 1. use dictionary but it will use extra space O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = {}
        for i, val in enumerate(numbers):
            if target - numbers[i] not in idx:
                idx[val] = i
            else:
                return sorted([i + 1, idx[target - numbers[i]] + 1])

# 2. two pointers from ends to middle, like 15.3Sum
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        
        while l <= r:
            curr_sum = numbers[l] + numbers[r]
            
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return [-1, -1]