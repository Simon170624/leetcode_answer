# tree using dfs
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lower = float('-inf')
        upper = float('inf')
        
        return self.dfs(root, lower, upper)
    
    def dfs(self, root, lower, upper):
        
        val = root.val
        if val <= lower or val >= upper:
            return False
        
        if not root.left and not root.right:
            return True
        elif root.left and root.right:
            return self.dfs(root.left, lower, val) and self.dfs(root.right, val, upper)
        elif not root.left and root.right:
            return self.dfs(root.right, val, upper)
        else: # root.left and not root.right
            return self.dfs(root.left, lower, val)
# First think list to solve tree problems
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.res = []
        self.dfs(root)
        return len(set(self.res)) == len(self.res) and sorted(self.res) == self.res
    
    def dfs(self, root):
        if not root:
            return None
        
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)