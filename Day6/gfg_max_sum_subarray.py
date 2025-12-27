# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
class Solution:
    def maxSubarraySum(self, arr, k):
        low = 0
        high = k - 1
        max_sum = float('-inf')
    
        if high == len(arr) - 1:
            return sum(arr)
        present_sum = sum(arr[low: high+1])
        while(high < len(arr)):
            if present_sum > max_sum:
                max_sum = present_sum
    
            if high + 1 > len(arr) - 1:
                break
            present_sum = present_sum - arr[low] + arr[high+1]
            low += 1
            high += 1
    
        return max_sum