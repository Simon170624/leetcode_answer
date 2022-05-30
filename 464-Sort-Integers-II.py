# quick sort, O(nlogn) time + O(1) memory
class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        self.quickSort(a, 0, len(a) - 1)
    
    def quickSort(self, a, start, end):
        if start >= end:
            return
        
        left, right = start, end
        # key point 1: pivot is the value, not the index
        pivot = a[(start + end) // 2];

        # key point 2: every time you compare left & right, it should be 
        # left <= right not left < right
        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            
            while left <= right and a[right] > pivot:
                right -= 1
            
            if left <= right:
                a[left], a[right] = a[right], a[left]
                
                left += 1
                right -= 1
        
        self.quickSort(a, start, right)
        self.quickSort(a, left, end)