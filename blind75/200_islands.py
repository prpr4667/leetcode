# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1


import collections


class Solution:
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        count_islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r1, c1 = row + dr, col + dc
                    if (
                        r1 >= 0
                        and r1 < ROWS
                        and c1 >= 0
                        and c1 < COLS
                        and grid[r1][c1] == "1"
                    ):
                        q.append((r1, c1))
                        grid[r1][c1] = "-1"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count_islands += 1

        return count_islands


solution = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(solution.numIslands(grid))
