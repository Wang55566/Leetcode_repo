from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        def reverse(string):
            res = ""
            for i in range(len(string) - 1, -1, -1):
                res += string[i]
            return res

        new = set(nums)
        for num in nums:
            string = str(num)
            # reversed = string[::-1]
            reversed = reverse(string)
            new.add(int(reversed))


        return len(new)
