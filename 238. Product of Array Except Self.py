# 1. import useful libraries
# time complexity: O(n^3), space complexity: O(n)
import numpy as np
import collections

nums = [1, 2, 3, 4]
q = collections.deque(nums)
res = []

for _ in range(len(nums)):
    tmp = q.popleft()
    curr_ls = list(q)
    res.append(np.prod(curr_ls))
    q.append(tmp)

print(res)

# 2. data structures and algorithms
# time complexity: O(n), space complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res