# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        _sum = 0

        def dfs(node):
            nonlocal _sum
            if not node:
                return
            
            if low <= node.val <= high:
                _sum += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

        dfs(root)
        return _sum