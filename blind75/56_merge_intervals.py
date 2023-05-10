# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda i: i[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


sol = Solution()
intervals = [[1, 4], [4, 5]]
print(sol.merge(intervals))
