import heapq
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums.sort()
        maxHeap = [-x for x in nums]
        print(maxHeap)
        heapq.heapify(maxHeap)
        print(maxHeap)
        num1 = heapq.heappop(maxHeap)
        num2 = heapq.heappop(maxHeap)
        print(num1, num2)
        return (-num1 - 1) * (-num2 - 1)
