# https://leetcode.com/problems/minimum-window-substring/description/

def check(s_count, t_count):
    for i in range(128):
        if s_count[i] < t_count[i]:
            return False
    return True
        
def minWindow(s, t):
    t_count = [0]*128
    s_count = [0]*128

    for ch in t:
        t_count[ord(ch)] += 1

    low = 0
    start = 0
    best = float('inf')

    for high in range(len(s)):
        s_count[ord(s[high])] += 1
        
        while check(s_count, t_count):
            if high - low + 1 < best:
                best = high - low + 1
                start = low
            s_count[ord(s[low])] -= 1
            low += 1
    if best == float('inf'):
        return ""
    return s[start:start+best]

s = 'ADOBECODEBANC'
t = 'ABC'
print(minWindow(s,t))