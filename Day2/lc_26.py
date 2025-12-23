class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low_pt = 0
        up_pt = 1

        while up_pt < len(nums):
            if nums[up_pt] == nums[low_pt]:
                up_pt += 1
            else:
                nums[low_pt + 1] = nums[up_pt]
                up_pt += 1
                low_pt += 1
        
        return low_pt+1
                
