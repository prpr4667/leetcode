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
        q1, q2 = collections.deque(), collections.deque()
        q1.append(original)
        q2.append(cloned)

        while q1:
            size = len(q1)
            for _ in range(size):
                node1 = q1.popleft()
                node2 = q2.popleft()
                if node1 == target:
                    return node2
                if node1.left:
                    q1.append(node1.left)
                    q2.append(node2.left)
                if node1.right:
                    q1.append(node1.right)
                    q2.append(node2.right)