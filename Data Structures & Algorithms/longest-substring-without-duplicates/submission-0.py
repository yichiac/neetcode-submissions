class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, two pointers
        left = 0
        sublen = 0
        mp = {}

        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]]+1, left)
            mp[s[right]] = right
            sublen = max(sublen, right - left + 1)
        return sublen