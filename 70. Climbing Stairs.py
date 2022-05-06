# recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return None
        
        return self.helper(n)
    
    def helper(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.helper(n - 1) + self.helper(n - 2)

# create a list
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        steps = [1, 2]
        for i in range(2, n):
            steps.append(steps[i - 1] + steps[i - 2])
        
        return steps.pop()