class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        new_set = set()
        missing_num = 0
        for i in range(len(nums)):
            if nums[i] not in new_set:
                new_set.add(nums[i])
            else:
                duplicated_num = nums[i]


        for i in range(1,len(nums)+1):
            if i not in nums:
                print(i)
                missing_num = i

        return [duplicated_num,missing_num]
