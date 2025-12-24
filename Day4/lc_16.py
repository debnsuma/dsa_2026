# https://leetcode.com/problems/3sum-closest/submissions/1864545122/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        i = 0 
        max_diff = float('inf')
        result = float('inf')

        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1
            while left < len(nums) and left < right:
                present_sum = nums[i] + nums[left] + nums[right]

                abs_diff = abs(present_sum - target)
                if abs_diff < max_diff:
                    max_diff = abs_diff 
                    result = present_sum

                if present_sum < target:
                    left += 1
                
                else:
                    right -= 1

            i += 1

        return result 