# Given a stream of numbers, print average (or mean) of the stream at every point.

def getAverage(prev_avg, val, n):
    return ((prev_avg * n) + val) / (n + 1)

def findAndPrintMovingAvgs(arr):
    cur_avg = 0
    for i in range(len(arr)):
        cur_avg = getAverage(cur_avg, arr[i], i)
        print "Avg at", i, "is", cur_avg

arr = [10, 20, 30, 40, 50]
findAndPrintMovingAvgs(arr)