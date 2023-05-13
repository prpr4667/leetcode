# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


class Solution:
    def maxPathSum(self, root) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            res = max(res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res
