class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res= []
        p1_idx, p2_idx= len(nums)-1, len(nums)-1
        # find p1_idx and p2_idx
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > 0:
                p1_idx = i
            elif nums[i]< 0:
                p2_idx = i

        while p1_idx < len(nums) and p2_idx < len(nums):
            res.append(nums[p1_idx])
            res.append(nums[p2_idx])
            p1_idx +=1
            p2_idx +=1
            #how to move p1_idx and p2_idx
            while p1_idx < len(nums) and nums[p1_idx] < 0:
                p1_idx +=1
            while p2_idx < len(nums) and nums[p2_idx] > 0:
                p2_idx +=1
        return res
