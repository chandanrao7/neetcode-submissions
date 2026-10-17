class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Solution1 using dict
        # res={}
        # for num in nums:
        #     res[num]=res.get(num,0)+1
        # res=sorted(res.items(),key=lambda x:x[1],reverse=True)
        # return res[0][0]
        #Solution 2 brute force
        length=len(nums)
        for num in nums:
            count=0
            for i in nums:
                if num==i:
                    count+=1
            if count>length//2:
                return num