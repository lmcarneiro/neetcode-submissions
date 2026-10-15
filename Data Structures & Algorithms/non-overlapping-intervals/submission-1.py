class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)
        remove = 0
        lastEnd = intervals[0][1]
        i = 1

        while i < len(intervals):
            start, end = intervals[i]
            if start >= lastEnd:
                lastEnd = end
            else:
                remove += 1
                lastEnd = min(end, lastEnd)
            i += 1

        return remove