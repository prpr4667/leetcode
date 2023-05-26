# Given two binary strings a and b, return their sum as a binary string.

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        _sum, carry = 0, 0
        sol = []
        idx = 0

        for idx in range(n - 1, -1, -1):
            _sum = int(a[idx]) + int(b[idx]) + carry
            sol.insert(0, str(_sum % 2))
            carry = _sum // 2
        if carry:
            sol.insert(0, str(carry))

        return "".join(sol)


solution = Solution()
a = "10101"
b = "1100"
print(solution.addBinary(a, b))
