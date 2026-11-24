class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # soluiton 1
        # for i in range(len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]
        # Solution 2
        r=0
        l=len(numbers)-1
        
        while r<l:
            curr=numbers[r]+numbers[l]
            if(curr==target):
                return [r+1,l+1]
            elif curr<target:
                r+=1
            else:
                l-=1
        return []
     