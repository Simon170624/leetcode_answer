class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        
        res = []
        while slow:
            res.append(slow.val)
            slow = slow.next
        
        if res == res[::-1]:
            return True
        else:
            return False