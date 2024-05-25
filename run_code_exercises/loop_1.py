def maxIncreasingGroups(usageLimits):
    maxGroup = 0
    sortedLimits = sorted(usageLimits)
    for index in range(0, len(usageLimits)):
        if sortedLimits[index] > index:
            maxGroup += 1
        else:
            break
    return maxGroup


def isRectangleCover(rectangles):
    minX = rectangles[0][0]
    minY = rectangles[0][1]
    maxA = rectangles[0][2]
    maxB = rectangles[0][3]
    maxWidth = maxA - minX
    maxHeight = maxB - minY
    maxArea = maxWidth * maxHeight
    curArea = maxArea
    for recIdx in range(1, len(rectangles)):
        rec = rectangles[recIdx]
        curX = rec[0]
        curY = rec[1]
        curA = rec[2]
        curB = rec[3]
        curWidth = curA - curX
        curHeight = curB - curY
        curArea += curWidth * curHeight
        minX = min(curX, minX)
        minY = min(curY, minY)
        maxA = max(curA, maxA)
        maxB = max(curB, maxB)
    maxWidth = maxA - minX
    maxHeight = maxB - minY
    maxArea = maxWidth * maxHeight
    return curArea == maxArea
