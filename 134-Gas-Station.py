# 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [gas[i] - cost[i] for i in range(len(gas))] 
        
        if sum(remain) < 0:
            return -1
        
        index = 0
        curr = 0
        for i in range(len(remain)):
            curr += remain[i]
            if curr < 0:
                curr = 0
                index = i + 1
        
        return index
# 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:  
        if sum(gas) - sum(cost) < 0:
            return -1
        
        index = 0
        curr = 0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                index = i + 1
        
        return index