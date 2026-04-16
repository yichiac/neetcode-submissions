class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            # odd-length
            ans += self.countPalindromAroundCenter(s, i, i)
            # even-length
            ans += self.countPalindromAroundCenter(s, i, i+1)
        return ans
    
    def countPalindromAroundCenter(self, s: str, lo: int, hi: int) -> int:
        ans = 0

        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
            ans += 1

        return ans