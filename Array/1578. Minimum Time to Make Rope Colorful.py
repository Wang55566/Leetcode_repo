from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        listColors = list(colors)

        if len(colors) == 1:
            return 0

        prev_i = 0
        curr_i = 1

        while curr_i < len(listColors):

            while curr_i < len(listColors) and listColors[prev_i] == listColors[curr_i]:

                if neededTime[prev_i] > neededTime[curr_i]:
                    res += neededTime[curr_i]
                    listColors.pop(curr_i)
                    neededTime.pop(curr_i)
                elif neededTime[prev_i] <= neededTime[curr_i]:
                    res += neededTime[prev_i]
                    listColors.pop(prev_i)
                    neededTime.pop(prev_i)

            prev_i += 1
            curr_i = prev_i + 1

        return res
