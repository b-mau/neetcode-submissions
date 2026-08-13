# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def depth(curr):    
            if curr is None:
                return 0
            
            l,r = depth(curr.left), depth(curr.right)
            if abs(l - r) > 1:
                self.balanced = False
            return 1 + max(l,r)
        
        depth(root)
        return self.balanced