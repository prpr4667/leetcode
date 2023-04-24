# Given an integer array nums, return the length of the longest strictly increasing
# subsequence.

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


class Solution:
    def lengthOfLIS(self, nums):
        lis = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for idx in range(i + 1, len(nums)):
                if nums[i] < nums[idx]:
                    lis[i] = max(lis[i], lis[idx] + 1)
        return max(lis)


solution = Solution()
nums = [0, 1, 0, 3, 2, 3]
print(solution.lengthOfLIS(nums))
