class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

            if hashmap[num] == 2:
                res.append(num)
        return res
