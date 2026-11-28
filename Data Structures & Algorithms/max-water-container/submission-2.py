class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Solution1 Brute force
        # res=0
        # for i in range(0,len(heights)):
        #     for j in range(i+1,len(heights)):
        #         res=max(res,(min(heights[i],heights[j])*(j-i)))
        # return res
        
        #Solution 2
        l=0
        r=len(heights)-1
        res=0
        while l<r:
            area= (min(heights[l], heights[r])) * (r-l)
            res=max(res,area)
            if(heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
        return res