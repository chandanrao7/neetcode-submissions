class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Solution 1 bad solution
        # nums=[abs(num) for num in nums]
        # nums=set(nums)
        # nums=list(nums)
        # nums.sort()
        # print(nums)
        # count=1
        # max_count=0
        # if len(nums)==0:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i+1]-nums[i]==1:
        #         count+=1
        #     else:
        #         if count>max_count:
        #             max_count=count
        #         count=0
        # max_count=max(count,max_count)
        # return max_count
        # Solution 2  Brute force
        #nums = [2,20,4,10,3,4,5]
        #        i  streak, res, curr  2->3
        #  streak 1 2  3  4  
        #  curr  2  3  4  5  6
        # numset=set(nums)
        # res=0
        # nums.sort()

        # for num in nums:
        #     streak=0
        #     curr=num
        #     while curr in numset:
        #         streak=streak+1
        #         curr=curr+1
        #     res=max(res,streak)
        # return res
        # Solution 3: Hashset
        # nums=[100, 4, 200, 1, 3, 2]
            
        numset=set(nums)
        longest=0
        for num in nums:
            if (num-1) not in numset:
                length=1
                while(num+length) in numset:     
                    length+=1
                longest=max(length,longest)
        return longest                        