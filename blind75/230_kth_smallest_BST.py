# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Input: root = [3,1,4,null,2], k = 1
# Output: 1


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest_rec(self, root, k: int) -> int:
        res = []
        
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res[k-1]
    
    def kthSmallest_iter(self, root, k: int) -> int:
        stack = []
        node = root

        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right