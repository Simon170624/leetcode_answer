class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        if not s:
            return result
        
        self.helper(result, [], 0, s)
        return result
        
    def is_palindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    def helper(self, result, path, index, s):
        if index == len(s):
            result.append(path[:])
            return
        
        for i in range(index, len(s)):
            substr = s[index : i + 1]
            if not self.is_palindrome(substr):
                continue
            path.append(substr)
            self.helper(result, path, i + 1, s)
            path.pop()