# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst(root,float('-inf'),float('inf'))
    def bst(self,root,minimum,maximum):
        if root is None:
            return True
        if root.val<=minimum or root.val>=maximum:
            return False
        return self.bst(root.left,minimum,root.val) and self.bst(root.right,root.val,maximum)