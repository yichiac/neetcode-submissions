class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cur_streak = 1
                while cur + 1 in num_set:
                    cur += 1
                    cur_streak += 1
                
                longest_streak = max(cur_streak, longest_streak)
        return longest_streak