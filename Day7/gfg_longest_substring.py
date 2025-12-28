# https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

class Solution:
    def longestKSubstr(self, string, k):
        low = 0 
        high = 0
        chars = {}
        res = float('-inf')
        while high < len(string):
            if chars.get(string[high]):
                chars[string[high]] += 1
            else:
                chars[string[high]] = 1
            
            while len(chars.keys()) > k :
                if chars[string[low]] == 1:
                    chars.pop(string[low])
                else:
                    chars[string[low]] -= 1
                low += 1
                # print(f"high = {high}, low = {low}, {chars}")
            
            if len(chars.keys()) == k:
                res = max(res,high - low + 1)
    
            high += 1
        
        res = max(res, -1)
        # print(res)
        return res
        

s = "aabaaab"
k = 2
longestKSubstr(s, k)