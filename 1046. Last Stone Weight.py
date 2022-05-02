# create max heap using min heap, nums = [-num for num in nums] 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        print(stones)
        heapq.heapify(stones)
        print(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])