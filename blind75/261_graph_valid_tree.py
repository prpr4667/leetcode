# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.


class Solution:
    def validTree(self, n: int, edges):
        if not n:
            return True

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for i in adj[node]:
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)


solution = Solution()
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(solution.validTree(n, edges))
