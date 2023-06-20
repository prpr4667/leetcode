# Given the root of a binary tree, return the sum of values of its deepest leaves.
 
# Example 1:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def deepestLeavesSum(self, root) -> int:
        q = collections.deque()
        q.append(root)
        _sum = 0

        while q:
            size = len(q)
            _sum = 0
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                _sum += node.val
            

        return _sum
        