# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


class Solution:
    def missingNumber(self, nums):
        xor = len(nums)

        for i, num in enumerate(nums):
            xor ^= i ^ num

        return xor

    def missingNumber_GF(self, nums):
        n = len(nums)
        sigma = (n * (n + 1)) // 2
        return sigma - sum(nums)


solution = Solution()
nums = [3, 0, 1, 4, 2, 6]
print(solution.missingNumber_GF(nums))
