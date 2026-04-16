class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            dist = right - left
            short_side = min(heights[left], heights[right])
            water = short_side * dist
            max_water = max(water, max_water)
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1

        return max_water