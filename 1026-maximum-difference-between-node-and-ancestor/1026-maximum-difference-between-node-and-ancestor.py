# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mn, mx):
            # Base Case: If we reach None, just return 0 in order not to affect the result
            if not root: return 0
            
			# The best difference we can do using the current node can be found:
            res = max(abs(root.val - mn), abs(root.val - mx))
			
			# Recompute the new minimum and maximum taking into account the current node
            mn, mx = min(mn, root.val), max(mx, root.val)
			
			# Recurse left and right using the newly computated minimum and maximum
            return max(res, dfs(root.left, mn, mx), dfs(root.right, mn, mx))
        
        # Initialize minimum `mn` and maximum `mx` equals value of given root
        return dfs(root, root.val, root.val)