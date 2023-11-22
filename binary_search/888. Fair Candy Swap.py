from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)

        bobSizes.sort()

        total_difference = total_bob - total_alice
        target = total_difference // 2

        for candy in aliceSizes:
            real_target = candy + target
            left = 0
            right = len(bobSizes) - 1

            while left <= right:

                middle = (left + right) // 2

                if bobSizes[middle] == real_target:
                    return [candy, real_target]
                elif bobSizes[middle] > real_target:
                    right = middle - 1
                elif bobSizes[middle] < real_target:
                    left = middle + 1
