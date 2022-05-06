class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0 :
            x = 1 / x  
            n = -n
        
        self.x = x
        res = self.helper(n)
        
        return res
    
    def helper(self, n):
        if n == 0:
            return 1
        if n == 1:
            return self.x
        
        res = self.helper(n // 2)
        
        if n % 2 == 1:
            res = self.x * (res ** 2) 
        else:
            res = res ** 2
        
        return res
        