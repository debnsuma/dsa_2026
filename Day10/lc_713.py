# https://leetcode.com/problems/subarray-product-less-than-k/

def numSubarrayProductLessThanK(nums, k):
    high = 0 
    low = 0
    product = 1
    result = 0

    while high < len(nums):
        product *= nums[high]

        while product >= k and low < high:
            product /= nums[low]
            low += 1
        
        if product < k:
            diff = high - low + 1
            result += diff
        high += 1


    print(result)
    return result

# nums = [10,5,2,6]
# k = 100
nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19

numSubarrayProductLessThanK(nums, k)