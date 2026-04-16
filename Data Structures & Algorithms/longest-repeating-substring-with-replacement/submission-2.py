class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointers
        maxlen = 0
        left = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            valid = (right - left + 1) - max(char_count.values())
            if valid <= k:
                maxlen = max(maxlen, right - left + 1)
            else:
                char_count[s[left]] -= 1
                left += 1

        return maxlen
        