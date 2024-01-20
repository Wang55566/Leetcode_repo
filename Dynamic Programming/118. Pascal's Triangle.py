from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res, prev_list = [[1]], [1]

        for i in range(1, numRows):
            sublist = []
            sublist.append(1)

            for j in range(len(prev_list) - 1):
                sublist.append(prev_list[j] + prev_list[j + 1])

            sublist.append(1)
            res.append(sublist)
            prev_list = sublist


        return res
