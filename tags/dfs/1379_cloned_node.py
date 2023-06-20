# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        s1, s2 = [original], [cloned]

        while s1:
            n1, n2 = s1.pop(), s2.pop()
            if n1 == target:
                return n2
            if n1.left:
                s1.append(n1.left)
                s2.append(n2.left)
            if n1.right:
                s1.append(n1.right)
                s2.append(n2.right)