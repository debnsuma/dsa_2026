# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        present_sum = 0
        min_len = float('inf')
        while high <= len(nums)-1:
            present_sum += nums[high]
            while present_sum >= target and low <= high:
                min_len = min(min_len, high - low + 1)
                low += 1
                present_sum = present_sum - nums[low-1] 
            high += 1
        if min_len == float('inf'):
            return 0
        return min_len





