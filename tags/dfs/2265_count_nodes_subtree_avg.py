# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

# Note:
# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.

def averageOfSubtree(self, root) -> int:
    result = 0

    def dfs(node):
        if not node:
            return 0, 0
        nonlocal result

        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)

        _sum = node.val + left_sum + right_sum
        count = 1 + left_count + right_count

        if _sum//count == node.val:
            result += 1

        return _sum, count
    
    dfs(root)
    return result