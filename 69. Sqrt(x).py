class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid > x:
                r = mid - 1
            elif mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            else: # (mid + 1) * (mid + 1) <= x
                l = mid + 1