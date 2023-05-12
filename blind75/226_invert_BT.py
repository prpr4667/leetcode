# Given the root of a binary tree, invert the tree, and return its root.


class Solution:
    def invertTree(self, root):
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
