class Solution:
    def reverseList(self, head):
        if not head:
            return head
        
        dummy = ListNode(-1)
        
        while head:
            new_node = ListNode(0)
            new_node.next = dummy.next
            val_node = ListNode(head.val)
            dummy.next = val_node
            val_node.next = new_node.next
            head = head.next
        
        return dummy.next