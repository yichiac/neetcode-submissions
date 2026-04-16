class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            # left sorted
            if nums[m] >= nums[l]: # need to review
                if target > nums[m] or target < nums[l]: # this is the hard part
                    l = m + 1
                else:
                    r = m - 1
            # right sorted
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1