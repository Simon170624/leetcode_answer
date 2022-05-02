# queue FIFO, stack FILO
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
        while len(q) != 0:
            curr_size = len(q)
            curr_list = []
            
            for _ in range(curr_size):
                node = q.popleft()
                curr_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(curr_list.pop())
        
        return res