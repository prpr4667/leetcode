# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Ex: Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution:
    def twoSum(self, nums, target: int):
        indexes = {}

        for i, n in enumerate(nums):
            if target - n in indexes:
                return [indexes[target - n], i]
            indexes[n] = i

        return [-1, -1]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
