# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_arr = []
        pos_arr = []
        new_arr = []

        for i in nums: 
            if i < 0: 
                neg_arr.append(i**2) 
            else: 
                pos_arr.append(i**2)

        neg_arr.reverse()
        i_neg = 0
        j_pos = 0 

        while i_neg < len(neg_arr) and j_pos < len(pos_arr):
            if neg_arr[i_neg] < pos_arr[j_pos]:
                new_arr.append(neg_arr[i_neg])
                i_neg += 1
            else:
                new_arr.append(pos_arr[j_pos])
                j_pos += 1
        
        if i_neg >= len(neg_arr):
            new_arr.extend(pos_arr[j_pos:])
        else:
            new_arr.extend(neg_arr[i_neg:])

        return new_arr       