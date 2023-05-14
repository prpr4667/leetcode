# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


class Solution:
    def levelOrder(self, root):
        q = collections.deque()
        q.append(root)
        res = []

        if not root:
            return res

        while q:
            size = len(q)
            lvl = []
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl.append(node.val)
            res.append(lvl)

        return res
