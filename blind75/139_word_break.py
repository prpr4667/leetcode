# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".


class Solution:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
        print(dp)
        return dp[0]


solution = Solution()
s = "abcd"
wordDict = ["a", "abc", "b", "cd"]
print(solution.wordBreak(s, wordDict))
