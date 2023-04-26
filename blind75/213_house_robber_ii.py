# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.


class Solution:
    def rob(self, nums):
        def house_rob(nums):
            h1, h2 = 0, 0

            for h in nums:
                _max = max(h1 + h, h2)
                h1 = h2
                h2 = _max
            return h2

        return max(nums[0], house_rob(nums[1:]), house_rob(nums[:-1]))


solution = Solution()
nums = [2, 7, 9, 3, 1]
print(solution.rob(nums))
