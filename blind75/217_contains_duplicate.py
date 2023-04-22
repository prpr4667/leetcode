# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true


class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        if len(nums) <= 1:
            return False

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


sol = Solution()
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(sol.containsDuplicate(nums))
