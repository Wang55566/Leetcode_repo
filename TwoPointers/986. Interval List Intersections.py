from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        indexOne, indexTwo = 0, 0

        while len(firstList) > indexOne and len(secondList) > indexTwo:
            start = max(firstList[indexOne][0], secondList[indexTwo][0])
            end = min(firstList[indexOne][1], secondList[indexTwo][1])

            if start <= end:
                res.append([start, end])
            if firstList[indexOne][1] < secondList[indexTwo][1]:
                indexOne += 1
            else:
                indexTwo += 1
        return res
