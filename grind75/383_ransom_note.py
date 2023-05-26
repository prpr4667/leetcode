# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = sorted(list(ransomNote))
        mag = sorted(list(magazine))

        i, j = 0, 0

        while i < len(rn) and j < len(mag):
            if mag[j] == rn[i]:
                i += 1
            j += 1
        return i == len(rn)
