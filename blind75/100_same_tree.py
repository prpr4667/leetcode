# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
