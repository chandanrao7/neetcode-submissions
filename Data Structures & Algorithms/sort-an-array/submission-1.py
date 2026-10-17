class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Sol1: in built
        nums.sort()
        return nums
        #Sol2:
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
        
#[5,10,2,1,3]
# i
# j