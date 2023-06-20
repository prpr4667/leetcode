You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

class Solution:
    def getAverages(self, nums, k):
        k_avg = [-1] * len(nums)
        _sum = 0

        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                k_avg[i] = -1
                _sum += nums[i]
                continue
            else:
                print(i, _sum)
                k_avg[i] = _sum
                _sum += (nums[i] - nums[i-k])

        _sum = 0
        for i in range(len(nums)-1, -1, -1):
            if i - k < 0 or i + k >= len(nums):
                _sum += nums[i]
                continue
            else:
                k_avg[i] += (_sum + nums[i])
                k_avg[i] = k_avg[i] // (2*k+1)
                _sum += (nums[i] - nums[i+k])
        
        return k_avg
    
