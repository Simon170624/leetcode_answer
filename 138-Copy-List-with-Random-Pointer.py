class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        mapping = {}
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        for key in mapping.keys():
            if key.next:
                mapping[key].next = mapping[key.next]
            if key.random:
                mapping[key].random = mapping[key.random]
        
        return mapping[head]