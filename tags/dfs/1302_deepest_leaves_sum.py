# Given the root of a binary tree, return the sum of values of its deepest leaves.
 
# Example 1:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root) -> int:
        _sum = max_depth = 0
        stack = [(root, 0)]

        while stack:
            node, curr_depth = stack.pop()
            if not node.left and not node.right:
                if curr_depth > max_depth:
                    max_depth = curr_depth
                    _sum = node.val
                elif curr_depth == max_depth:
                    _sum += node.val
            else:
                if node.left:
                    stack.append((node.left, curr_depth+1))
                if node.right:
                    stack.append((node.right, curr_depth+1))
        
        return _sum

