class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1st solution
        # set1=set(nums)
        # if len(nums)==len(set1):
        #     return False
        # return True
        #2nd solution
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        #3rd solution
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False