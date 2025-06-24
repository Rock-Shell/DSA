class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_overlap(x,y):
            if x[1] >= y[0]:
                return True
            return False

        n = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)

        i = 0
        while i<len(intervals)-1:
            if is_overlap(intervals[i], intervals[i+1]):
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i+1)
            else:
                i+=1
        return intervals
