# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root) -> int:
        _sum = 0
        def dfs(node, p, gp):
            nonlocal _sum
            if not root:
                return 0

            if gp % 2 == 0:
                print(node.val)
                _sum += node.val
            if node.left:
                dfs(node.left, node.val, p) 
            if node.right:
                dfs(node.right, node.val, p)
        
        dfs(root, -1, -1)
        return _sum