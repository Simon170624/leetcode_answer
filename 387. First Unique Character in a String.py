# Counter can create dictionary based on string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = Counter(s)
        
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
            
        return -1