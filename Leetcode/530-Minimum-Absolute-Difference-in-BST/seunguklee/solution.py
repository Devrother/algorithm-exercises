# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Binaray Search Tree 성질 : inorder -> 오름차순 정렬이 됨!
    def getMinimumDifference(self, root: 'TreeNode') -> 'int':
        L: List[int] = list()
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            L.append(root.val)
            inorder(root.right)
        inorder(root)
        return min(abs(a - b) for a, b in zip(L, L[1:]))

