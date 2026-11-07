# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        pre_i = 0  # next root to consume from preorder

        def build(lo, hi):  # builds the subtree for inorder[lo..hi]
            nonlocal pre_i
            if lo > hi:
                return None
            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)
            mid = idx[root_val]
            root.left = build(lo, mid - 1)   # must come before right
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)