# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        char_count = [0] * 26 
        low = 0
        max_len = float('-inf')

        for high in range(len(string)):
            idx = ord(string[high]) - ord('A')
            char_count[idx] += 1
            lenght = high - low + 1
            diff = lenght - max(char_count)

            while diff > k:
                idx = ord(string[low]) - ord('A')
                char_count[idx] -= 1
                low += 1
                lenght = high - low + 1
                diff = lenght - max(char_count)
            
            max_len = max(max_len, lenght)

        print(max_len)
        return max_len




