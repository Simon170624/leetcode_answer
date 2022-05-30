# recursion leads to time limit exceeded
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        return self.dfs(0, s, wordDict)
    
    def dfs(self, start_index, s, wordDict):
        if start_index == len(s):
            return True
        
        for word in wordDict:
            if start_index + len(word) > len(s):
                continue 
            
            if s[start_index: start_index + len(word)] == word:
                if self.dfs(start_index + len(word), s, wordDict):
                    return True 
        return False
# DP is faster than recursion
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        
        max_length = max([len(word) for word in wordDict])
        dp = [False] * (len(s) + 1 + max_length)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(1, max_length + 1):
                if s[i - 1 : i + j - 1] in wordDict and dp[i - 1]:
                    # print(i, j, dp)
                    dp[i + j - 1] = True
                
        # print(dp)
        return dp[len(s)]