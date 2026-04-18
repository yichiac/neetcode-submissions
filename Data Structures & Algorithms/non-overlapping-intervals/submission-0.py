class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sorting by the start time
        intervals.sort()
        count = 0
        prevend = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                count += 1
                prevend = min(end, prevend)
        
        return count