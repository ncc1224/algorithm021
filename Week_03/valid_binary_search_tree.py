# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root,lower=float("-inf"),higher=float("inf")):
        if not root: return True
        if root.val<=lower or root.val>=higher:return False
        left=self.isValidBST(root.left,lower,root.val)
        right=self.isValidBST(root.right,root.val,higher)
        return True if left and right else False



class Solution0:
    def isValidBST(self, root):
        stack,pre=[],float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val<=pre:return False
            pre=root.val
            root=root.right
        return True
