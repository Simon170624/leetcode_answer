# 1. not completed
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, 1
        min_height = max()
        
        while r < len(height):
            if height[r] > height[l]:
                print(height[l + 1: r])
                res += (r - l - 1) * min(height[l], height[r]) - sum(height[l + 1: r])
                l = r
                r += 1
            elif height[r] == height[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return res
# 2. opposite direction two pointers
# 
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

# 3. min(l, r) - h[i]
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        
        max_left = [0]
        for i in range(1, len(height)):
            max_left.append(max(height[0: i]))
        
        max_right = []
        for i in range(0, len(height) - 1):
            max_right.append(max(height[i + 1: len(height)]))
        max_right.append(0)
        
        min_l_r = []
        for i in range(len(height)):
            min_l_r.append(min(max_right[i], max_left[i]))
        
        res = 0
        for i in range(len(height)):
            if min_l_r[i] > height[i]:
                res += (min_l_r[i] - height[i])
        
        return res