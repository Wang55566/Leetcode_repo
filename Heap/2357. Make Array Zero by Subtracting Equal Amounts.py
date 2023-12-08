from typing import List
import heapq

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        heapq.heapify(nums)
        while nums:

            # heappop until we find the first non-zero integer
            num = heapq.heappop(nums)  # 2
            while nums and num == 0:
                num = heapq.heappop(nums)
            if num != 0:
                res += 1
            for i in range(len(nums)):
                nums[i] -= num
        return res
