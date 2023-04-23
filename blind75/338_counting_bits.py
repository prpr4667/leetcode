# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10


class Solution:
    def countBits(self, n):
        return [self.countSetBits(i) for i in range(n + 1)]

    def countSetBits(self, n):
        bits_set = 0
        while n > 0:
            if n & 1:
                bits_set += 1
            n >>= 1
        return bits_set


solution = Solution()
n = 5
print(solution.countBits(n))
