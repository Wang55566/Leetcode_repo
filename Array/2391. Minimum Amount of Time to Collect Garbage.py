from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        res = 0

        garbageList = ['G', 'P', 'M']

        for garbage_str in garbage:
            res += len(garbage_str)

        i = len(garbage) - 1
        while i >= 0:
            j = 0
            while j < len(garbageList):
                if garbageList[j] in garbage[i]:
                    res += sum(travel)
                    garbageList.pop(j)
                else:
                    j+=1
            if len(travel) != 0:
                travel.pop()
            i-=1

        return res
