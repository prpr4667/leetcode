# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are 
# sorted lexicographically
#  by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.


# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"


class Solution:
    def alienOrder(self, words):
        