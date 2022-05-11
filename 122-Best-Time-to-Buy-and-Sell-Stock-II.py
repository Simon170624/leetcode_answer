# brute force, O(n)
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
        
        l, r = 0, 1
        max_price = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                max_price += (prices[r] - prices[l])
                l = r
                r += 1
        
        return max(max_price, res)
# sell if i > i - 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                profit += prices[i] - prices[i - 1]
                
        return profit