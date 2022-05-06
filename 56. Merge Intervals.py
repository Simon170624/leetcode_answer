# simulation
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2: 
            return intervals  

        intervals.sort() 
        
        res = [] 
        start = intervals[0][0] 
        end = intervals[0][1] 
        
        for i in range(1, len(intervals)): 
            if intervals[i][0] <= end:  
                end = max(intervals[i][1], end) 
            else: 
                res.append([start, end])
                start = intervals[i][0] 
                end = intervals[i][1]
            
        res.append([start, end])  
        return res
        