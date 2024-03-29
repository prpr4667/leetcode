# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6


class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum, curr_sum = nums[0], 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num

            max_sum = max(max_sum, curr_sum)
        return max_sum


solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums))
