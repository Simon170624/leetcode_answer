#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
            
        return res
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else: # prices[r] >= prices[l]
                res = max(res, prices[r] - prices[l])
                r += 1
        
        return res