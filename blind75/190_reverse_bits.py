# Reverse bits of a given 32 bits unsigned integer.

# Example 1:

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.


class Solution:
    def reverseBits(self, n):
        bits = str(bin(n)[2:])
        print(bits)
        bits = bits[::-1].ljust(32, "0")
        print(bits)
        return int(bits, 2)
