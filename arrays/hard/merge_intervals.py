# https://leetcode.com/problems/merge-intervals/submissions/1221790448/
def merge(intervals):
    intervals.sort()
    output = []
    i = intervals[0][0]
    j = intervals[0][1]
    for item in intervals[1:]:
        if item[0] <= j:
            if item[1]>j:
                j = item[1] 
            continue
        else:
            output.append([i,j])
            i = item[0]
            j = item[1]
    output.append([i,j])
    return output
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
