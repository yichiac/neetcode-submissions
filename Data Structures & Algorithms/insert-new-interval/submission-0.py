class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 3 cases: 
        # 1: no overlapping before insert
        # 2: overlapping and merging
        # 3: no overlapping after insert

        n = len(intervals)
        i = 0
        res = []

        # case 1:
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # case 2:
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        
        # case 3:
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res