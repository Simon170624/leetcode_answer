class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return not subRoot
        
        if root.val == subRoot.val and self.helper(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def helper(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        return root.val == subRoot.val and self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)