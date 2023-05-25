# Given a binary tree, determine if it is height-balanced


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return (0, True)

            lHeight = height(node.left)
            rHeight = height(node.right)

            balanced = abs(lHeight[0] - rHeight[0]) <= 1 and (lHeight[1] and rHeight[1])

            return (1 + max(lHeight[0], rHeight[0]), balanced)

        return height(root)[1]
