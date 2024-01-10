class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        paired_nums = []
        for i in range(len(nums)//2):
            paired_nums.append(nums[i]+nums[len(nums)-1-i])
        return max(paired_nums)
