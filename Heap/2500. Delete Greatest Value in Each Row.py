import heapq
from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        # Make a new Grid with maxheap in every row
        newGrid = []
        for i in range(len(grid)):
            maxHeap = [-x for x in grid[i]]
            heapq.heapify(maxHeap)
            newGrid.append(maxHeap)

        while len(newGrid[0]) > 0:
            maximun = float('inf')
            for i in range(len(newGrid)):
                num = heapq.heappop(newGrid[i])
                if num < maximun:
                    maximun = num
            res += -maximun

        return res
