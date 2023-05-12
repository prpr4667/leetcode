# Given the root of a binary tree, invert the tree, and return its root.


class Solution:
    def invertTree(self, root):
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree_BFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
