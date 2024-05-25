import math


def findValidSplit(nums):
    arrLen = len(nums)
    for i in range(0, arrLen - 1):
        prefixValue = nums[0]
        suffixValue = nums[i + 1]
        for j in range(1, i + 1):
            prefixValue *= nums[j]
        for t in range(i + 2, arrLen):
            suffixValue *= nums[t]

        print(
            f"prefix - {prefixValue} -- suffix - {suffixValue} -- gcd - {math.gcd(suffixValue, prefixValue)}"
        )

        if math.gcd(suffixValue, prefixValue) == 1:
            return i

    return -1


# findValidSplit([4, 7, 8, 15, 3, 5])

from collections import deque

def maximumRobots(chargeTimes, runningCosts, budget):
  for k in range(0, len(chargeTimes)):
    robotCount = k+1
    price = max(chargeTimes[:robotCount]) + robotCount * sum(runningCosts[:robotCount])
    print(f"{chargeTimes[:robotCount]} - {runningCosts[:robotCount]} - price - {price}")
    if price > budget:
      return robotCount - 1

  return -1  

maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25)
print('------------------------------------------')
maximumRobots([11,12,19], [10,8,7], 19)
