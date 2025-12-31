# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        high = 0
        low = 0 
        max_len = float('-inf')
        state = {0: 0, 
                1: 0}
        for high in range(len(nums)):
            state[nums[high]] += 1
            length = high - low + 1
            diff = length - state[1]

            while diff > k:
                state[nums[low]] -= 1
                low += 1
                length = high - low + 1
                diff = length - state[1]
            
            max_len = max(max_len, length)

        print(max_len)
        return max_len

