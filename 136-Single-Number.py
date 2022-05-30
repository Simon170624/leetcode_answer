# 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        for key, val in nums_dict.items():
            if val == 1:
                return key

#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : XOR ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # If we take XOR of zero and some bit, it will return that bit
        # a XOR 0 = a, a XOR 0=a
        # If we take XOR of two same bits, it will return 0
        # a XOR a = 0 a XOR a=0
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b 
        # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        # So we can XOR all bits together to find the unique number.
        
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
            
        return nums[0]