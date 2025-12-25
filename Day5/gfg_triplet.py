# https://leetcode.com/problems/3sum-smaller/description/
# https://www.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1

class Solution:
    def countTriplets(self, n, target, arr):
        arr.sort()
        ans = 0
        i = 0
        
        while i < n - 2:
            left = i + 1
            right = n - 1
    
            while left <= right:
                present_sum = arr[i] + arr[left] + arr[right]
                if present_sum < target : 
                    ans += right - left 
                    left += 1
                else: 
                    right -= 1
            
            i += 1
            
        return ans

