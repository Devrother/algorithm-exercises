# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
inorder : left self right
preorder : self left right
postorder : left right self
"""
class Solution:
    def inorderTraversal(self, root):
        cur, stack, res = root, [], []
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res

