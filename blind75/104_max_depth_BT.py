# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


class Solution:
    def maxDepth_Rec(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0

        lvl = 0
        q = collections.deque()
        q.append(root)

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1

        return lvl

    def maxDepth_DFS(self, root: Optional[TreeNode]) -> int:
        # DFS
        stack = []
        stack.append([root, 1])
        depth = 0

        while stack:
            node, curr_depth = stack.pop()

            if node:
                depth = max(depth, curr_depth)
                stack.append([node.left, curr_depth + 1])
                stack.append([node.right, curr_depth + 1])

        return depth
