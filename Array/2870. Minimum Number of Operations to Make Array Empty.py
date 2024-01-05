from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = {}

        for num in nums:
          if num in mp:
              mp[num] += 1
          else:
              mp[num] = 1


        count = 0
        for t in mp.values():
            if t == 1:
                return -1
            count += t // 3
            if t % 3:
                count += 1

        return count
