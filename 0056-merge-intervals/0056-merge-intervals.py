class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]

        for s,e in intervals:
            lastEnd=res[-1][1]
            if s<=lastEnd:
                res[-1][1]=max(lastEnd,e)
            else:
                res.append([s,e])
        return res