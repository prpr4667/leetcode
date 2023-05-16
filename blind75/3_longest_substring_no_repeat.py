# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res


solution = Solution()
s = "pwwkew"
print(solution.lengthOfLongestSubstring_1(s))
