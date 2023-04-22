# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.


class Solution:
    def maxProduct(self, nums) -> int:
        _max, _min = nums[0], nums[0]
        sol = _max

        for i in range(1, len(nums)):
            num = nums[i]
            (_min, _max) = (
                min(num, _min * num, _max * num),
                max(num, _min * num, _max * num),
            )
            sol = max(sol, _max)
        return sol


solution = Solution()
nums = [-2, 0, -1]
print(solution.maxProduct(nums))
