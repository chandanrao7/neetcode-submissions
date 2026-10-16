class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []
        # Solution2
        a=[]
        for index, values in enumerate(nums):
            a.append([index, values])
        a.sort(key=lambda x:x[1])

        i,j=0,len(nums)-1
        while i<j:
            curr=a[i][1]+a[j][1]
            print("Left:", a[i], "Right:", a[j], "Sum:", curr)
            if curr==target:
                return sorted([a[i][0],a[j][0]])
            elif curr<target:
                i+=1
            else:
                j-=1
        return []
       