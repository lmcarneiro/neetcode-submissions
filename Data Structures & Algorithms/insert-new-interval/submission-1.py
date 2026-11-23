class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            start, end = interval[0], interval[1]
            new_start, new_end = newInterval[0], newInterval[1]
            if new_end < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif new_start > end:
                res.append(interval)
            else:
                newInterval = [min(new_start, start), max(new_end, end)]
            
        res.append(newInterval)

        return res