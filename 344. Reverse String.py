# 1.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[::-1] = s

# 2. two pointer from end to middle
class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1