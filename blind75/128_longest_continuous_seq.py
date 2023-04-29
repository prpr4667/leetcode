# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        lcs = 0

        for n in nums:
            if n - 1 not in nums_set:
                length = 0

                while n + length in nums_set:
                    length += 1
                lcs = max(lcs, length)
        return lcs


solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(solution.longestConsecutive(nums))
