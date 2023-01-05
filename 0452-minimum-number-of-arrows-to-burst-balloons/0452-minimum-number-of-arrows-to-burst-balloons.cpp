class Solution:
    def findMinArrowShots(self, points):
        n = len(points)
        if n<2:
            return n

        #sort by start and end point
        START, END = 0,1
        points.sort(key=lambda i: (i[START],i[END]) )
        prev, cur = points[0], None
        darts = 0

        for i in range(1, n):
            cur = points[i]

            if cur[START] <= prev[END]:
                #overlap, wait for more overlap to throw dart
                prev = [cur[START], min(cur[END],prev[END])]
            else:
                #no overlap, throw dart at previous
                darts += 1
                prev = cur
		
		#pop the last balloon and return
        return darts+1