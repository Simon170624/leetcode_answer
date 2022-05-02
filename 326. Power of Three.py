class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            if n % 3 != 0:
                return False
                break
            else:
                n = n / 3
        
        if n == 1:
            return True
        else:
            return False