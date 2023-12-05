from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        storage = []     # (numbers of soilders, index)
        res = []

        for i in range(len(mat)):

            nums_of_soilders = 0

            for j in range(len(mat[0])):

                if mat[i][j] == 1:
                    nums_of_soilders += 1

            storage.append((nums_of_soilders, i))

        new = [( x, y ) for x, y in storage]
        heapq.heapify(new)

        for i in range(k):
            nums1, num2 = heapq.heappop(new)   # (num1, num2)
            res.append(nums1)

        return res
