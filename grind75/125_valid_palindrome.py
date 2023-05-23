# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


class Solution:
    def isPalindrome_1(self, s: str) -> bool:
        reversed = "".join([c.lower() for c in s if c.isalnum()])
        return reversed == reversed[::-1]

    def isPalindrome_2pointers(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True


solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome_2pointers(s))
