class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)

        for num in nums:
            res[num]+=1
        
        res_sorted=sorted(res.items(),key=lambda x:x[1],reverse=False)
        
        final=[]
        while len(final)<k:
            final.append(res_sorted.pop()[0])
        return final