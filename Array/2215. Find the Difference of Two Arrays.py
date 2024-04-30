from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []

        temp1 = set()
        for n in nums1:
            if n not in nums2:
                temp1.add(n)
        res.append(temp1)
        temp2 = set()
        for n in nums2:
            if n not in nums1:
                temp2.add(n)
        res.append(temp2)

        return res
