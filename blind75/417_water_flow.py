# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        visited_p, visited_a = set(), set()

        def dfs(r, c, visited, prev):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or heights[r][c] < prev
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, visited_p, heights[0][c])
            dfs(ROWS - 1, c, visited_a, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, visited_p, heights[r][0])
            dfs(r, COLS - 1, visited_a, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_a and (r, c) in visited_p:
                    res.append([r, c])

        return res


solution = Solution()
heights = [[1]]
print(solution.pacificAtlantic(heights))
