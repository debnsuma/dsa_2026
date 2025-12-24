# https://leetcode.com/problems/3sum/ 
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array 
        nums.sort()

        result = []
        i = 0
        print(nums)
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            k = len(nums) - 1
            while j < len(nums) and j < k:
                two_sum = nums[j] + nums[k]
                if two_sum == -nums[i]:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
                    while k < len(nums) - 1 and j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif two_sum < -nums[i]:
                    j += 1
                else:
                    k -= 1
            i += 1
        
        return result
