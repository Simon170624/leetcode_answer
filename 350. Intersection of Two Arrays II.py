# 1. two dictionaries
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):

        return (Counter(nums1) & Counter(nums2)).elements()
# 2. one dictionary
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []
        
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        
        return res