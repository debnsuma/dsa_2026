# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0
        end = len(numbers) - 1

        while start < end:
            present_sum = numbers[start] + numbers[end]
            if present_sum == target:
                return (start+1, end+1)
            elif present_sum > target:
                end -=1
            elif present_sum < target:
                start += 1
        return  

