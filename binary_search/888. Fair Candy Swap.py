from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)

        total_difference = total_bob - total_alice  #2
        target = total_difference // 2  # 2/2 = 1

        for candy in aliceSizes:  # [1, 1]
            real_target = candy + target   # 1 + 1 = 2
            # real_target = total_difference - candy
            print(candy, target)
            left = 0
            right = len(bobSizes) - 1

            while left <= right:
                middle = (left + right) // 2
                # print(left, middle, right, bobSizes[middle], real_target)
                if bobSizes[middle] == real_target:
                    return [candy, real_target]
                elif bobSizes[middle] > real_target:
                    right = middle - 1
                elif bobSizes[middle] < real_target:
                    left = middle + 1
