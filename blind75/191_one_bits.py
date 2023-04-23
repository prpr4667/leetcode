# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.


class Solution:
    def hammingWeight(self, n):
        ones = 0
        while n > 0:
            if n & 1:
                ones += 1
            n >>= 1
        return ones


solution = Solution()
n = 123
print(solution.hammingWeight(n))
