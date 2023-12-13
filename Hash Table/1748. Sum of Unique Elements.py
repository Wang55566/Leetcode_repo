class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for num in nums:
            if num in hashMap:
                hashMap[num] +=1
            else:
                hashMap[num] = 1

        for key in hashMap:
            if hashMap[key] == 1:
                res += key

        return res
