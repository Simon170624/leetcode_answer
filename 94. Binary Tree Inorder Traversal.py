class Solution:
    def inorderTraversal(self, root):
        if not root:
            return None
        
        self.res = []
        self.helper(root)
        return self.res
        
        
    def helper(self, root):
        if not root:
            return None
        
        self.helper(root.left)        
        self.res.append(root.val)
        self.helper(root.right)