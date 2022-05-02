class Solution:
    def isPalindrome(self, a: str) -> bool:
        a = a.lower()
        a = list(a)
        a = [i for i in a if i.isalnum() == True]
        
        l, r = 0, len(a) - 1
        while l <= r:
            if a[l] == a[r]:
                l += 1
                r -= 1
            else:
                return False
        return True