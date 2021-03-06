# Runtime: 40 ms, faster than 99.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dicts = {}
        max_length = 0
        count = 0
        sub_start_index = 0
        
        for index, sub in enumerate(s):
            if (sub in dicts) and (dicts[sub] >= sub_start_index):
                if count > max_length:
                    max_length = count
                sub_start_index = dicts[sub] +1
                count = index - dicts[sub]
            else:
                count += 1 
            dicts[sub] = index
            
        return max(max_length,count)