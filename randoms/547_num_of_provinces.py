# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

class Solution:
    def findCircleNum(self, isConnected) -> int:
        visited = set()

        def dfs(idx):
            nonlocal visited
            stack = [idx]

            while stack:
                curr = stack.pop()
                visited.add(curr)
                for i, neighbor in enumerate(isConnected[curr]):
                    if neighbor == 1 and i not in visited:
                        stack.append(i)
        
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces


solution = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(solution.findCircleNum(isConnected))