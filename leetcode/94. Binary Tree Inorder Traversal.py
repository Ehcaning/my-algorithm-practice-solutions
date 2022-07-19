# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root or root.val is None:
            return []
        res = []
        if root.left is not None:
            res += self.inorderTraversal(root.left)

        res += [root.val]

        if root.right is not None:
            res += self.inorderTraversal(root.right)

        return res
