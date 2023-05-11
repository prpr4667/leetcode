# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

import heapq


def minMeetingRooms_withCount(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    s, e = 0, 0
    _max, count = 0, 0
    while s < len(intervals):
        if start[s] >= end[e]:
            count -= 1
            e += 1
        else:
            count += 1
            s += 1
        _max = max(_max, count)

    return _max


def minMeetingRooms_withHeap(intervals):
    free_rooms = []
    intervals.sort(key=lambda x: x[0])

    heapq.heappush(free_rooms, intervals[0][1])

    for i in intervals[1:]:
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, i[1])

    return len(free_rooms)


intervals = [[0, 30], [5, 10], [9, 15], [15, 20], [20, 25]]
print(minMeetingRooms_withHeap(intervals))
