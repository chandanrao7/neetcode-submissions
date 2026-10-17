class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res={}
        for num in nums:
            res[num]=res.get(num,0)+1
        res=sorted(res.items(),key=lambda x:x[1],reverse=True)
        return res[0][0]