class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # O(n)
        numsSet = set(nums1)
        res = []

        # O(n)
        for num in numsSet:
            if num in nums2:
                res.append(num)

        return res

# test push
