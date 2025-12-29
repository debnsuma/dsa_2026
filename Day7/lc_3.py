# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        low = 0 
        chars = {}
        max_len = float('-inf')

        for high in range(len(string)):
            if chars.get(string[high]):
                chars[string[high]] += 1
            else:
                chars[string[high]] = 1
            
            k = high - low + 1

            while len(chars) < k:
                if chars.get(string[low]) == 1:
                    chars.pop(string[low])
                else:
                    chars[string[low]] -= 1
                low += 1
                k = high - low + 1

            max_len = max(max_len, high - low + 1)
        print(chars)
        print(max_len)
        return max_len if max_len != float('-inf') else 0
