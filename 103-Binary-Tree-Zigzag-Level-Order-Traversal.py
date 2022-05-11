class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
        left_to_right = True
        
        while len(q) > 0:
            curr_size = len(q)
            curr_ls = []
            
            for _ in range(curr_size):
                node = q.popleft()
                curr_ls.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if left_to_right == True:
                res.append(curr_ls)
                left_to_right = False
            else:
                res.append(curr_ls[::-1])
                left_to_right = True
                
        return res