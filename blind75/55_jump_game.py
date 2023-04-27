# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index


class Solution:
    def canJump(self, nums):
        pass

    def canJump_Greedy(self, nums):
        dest = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= dest:
                dest = i

        return dest == 0

    def canJump_DFS(self, nums):
        n = len(nums) - 1
        visited = [0] * len(nums)
        visited[0] = 1
        i = 0

        while visited[n] != 1 and i <= n:
            if visited[i]:
                _range = nums[i]
                for j in range(_range):
                    if i + j + 1 <= n:
                        visited[i + j + 1] = 1
            i += 1
        return visited[n] == 1


solution = Solution()
nums = [0, 2, 3]
print(solution.canJump_DFS(nums))
