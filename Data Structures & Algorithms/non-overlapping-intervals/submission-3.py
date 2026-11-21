class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        res = 0

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            if start < last_end:
                res += 1
            else:
                last_end = end

        return res