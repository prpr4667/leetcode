# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

# Example 1:

# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2


class Solution:
    def countComponents_DFS(self, n, edges):
        components = 0
        visited = set()

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(adj, visited, node):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(adj, visited, neighbor)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(adj, visited, node)

        return components

    def countComponents_unionFind(self, n, edges):
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] < rank[p1]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


solution = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(solution.countComponents_DFS(n, edges))
