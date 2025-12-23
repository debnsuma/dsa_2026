# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low_pt = 0
        up_pt = 1
        count = 1

        while up_pt < len(nums):
            if nums[up_pt] == nums[low_pt] and count < 2:
                nums[low_pt + 1] = nums[up_pt]
                low_pt += 1
                up_pt += 1
                count += 1
            elif nums[up_pt] == nums[low_pt] and count >= 2:
                up_pt += 1
            else:
                nums[low_pt + 1] = nums[up_pt]
                up_pt += 1
                low_pt += 1
                count = 1

        return low_pt + 1           


        