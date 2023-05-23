# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: s = "anagram", t = "nagaram"
# Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

        for c in t:
            if c not in counts:
                return False
            else:
                counts[c] -= 1
            if counts[c] == 0:
                del counts[c]
        print(counts)
        return len(counts) == 0


sol = Solution()
s = "rat"
t = "car"
print(sol.isAnagram(s, t))
