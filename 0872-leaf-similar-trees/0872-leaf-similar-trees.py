class Solution:
    def __init__(self):
        self.n = []
        
    def dfs(self, root):
        if root:
			# checking if the node is leaf
            if not root.left and not root.right:  
				# appends the leaf nodes to the list - self.n 
                self.n.append(root.val)  
				
            self.dfs(root.left)
            self.dfs(root.right)
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.dfs(root1)
        a = self.n
        self.n = []
        self.dfs(root2)
        
        if a == self.n:
            return True
        else:
            return False