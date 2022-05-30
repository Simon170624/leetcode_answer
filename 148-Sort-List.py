# O(n) + O(nlogn) + O(n) = O(nlogn) time and O(n) memory
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        
        if not head:
            return None
        
        while head:
            res.append(head.val)
            head = head.next
        
        res = sorted(res)
        dummy = ListNode(-1)
        tail = dummy
        for value in res:
            new_node = ListNode(value)
            tail.next = new_node
            tail = tail.next
        
        return dummy.next
# O(nlogn) time and O(1) memory using quick sort; merge sort need O(nlogn) time and O(n) memory
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
            
        fast = head
        slow = head
        
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        
        list1 = self.sortList(head)
        list2 = self.sortList(mid)
        
        sorted = self.merge(list1, list2)
        
        return sorted
    
    def merge(self, list1, list2):
            if list1 == None:
                return list2
            if list2 == None:
                return list1
        
            dummy = ListNode(0)
            tmp = dummy
            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    tmp.next = list1
                    list1 = list1.next
                else:
                    tmp.next = list2
                    list2 = list2.next
                tmp = tmp.next
            if list1 != None:
                tmp.next = list1
            else:
                tmp.next = list2
            return dummy.next
