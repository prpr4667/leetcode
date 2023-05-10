# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]


class Solution:
    def insert(self, intervals, newInterval):
        res = []

        for idx in range(len(intervals)):
            if newInterval[0] > intervals[idx][1]:
                res.append(intervals[idx])
            elif newInterval[1] < intervals[idx][0]:
                res.append(newInterval)
                return res + intervals[idx:]
            # interval merges with the new interval
            else:
                newInterval = [
                    min(intervals[idx][0], newInterval[0]),
                    max(intervals[idx][1], newInterval[1]),
                ]

        res.append(newInterval)
        return res


sol = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(sol.insert(intervals, newInterval))
