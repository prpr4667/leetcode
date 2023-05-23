# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


class Solution:
    def floodFill(self, image, sr, sc, color):
        def dfs(sr, sc, val, color):
            if (
                0 <= sr < len(image)
                and 0 <= sc < len(image[0])
                and image[sr][sc] == val
            ):
                if image[sr][sc] == color:
                    return
                image[sr][sc] = color
                dfs(sr + 1, sc, val, color)
                dfs(sr - 1, sc, val, color)
                dfs(sr, sc + 1, val, color)
                dfs(sr, sc - 1, val, color)

            else:
                return

        dfs(sr, sc, image[sr][sc], color)
        return image


solution = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(solution.floodFill(image, sr, sc, color))
