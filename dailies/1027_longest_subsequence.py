# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

# Note that:

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

class Solution:
    def longestArithSeqLength(self, nums) -> int:
        if not nums:
            return 0
        
        _range = max(nums) - min(nums)
        dp = [[1 for _ in range(2 * _range + 1)] for _ in range(len(nums))]
        _max = 1

        for i in range(len(nums)):
            for j in range(i):
                diff = _range + nums[i] - nums[j]
                dp[i][diff] = dp[j][diff] + 1
                _max = max(_max, dp[i][diff])
                
        return _max
    
sol = Solution()
ums = [2,2,2]
print(sol.longestArithSeqLength(ums))