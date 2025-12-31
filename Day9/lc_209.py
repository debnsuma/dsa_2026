# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        high = 0
        low = 0
        min_len = float('inf')
        present_sum = 0
        while high < len(nums):
            present_sum = present_sum + nums[high]

            while present_sum >= target:
                min_len = min(min_len, high-low+1)
                low += 1
                present_sum = present_sum - nums[low-1]
            
            high += 1
        return 0 if min_len == float('inf') else min_len 


