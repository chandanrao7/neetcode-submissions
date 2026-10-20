class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict=defaultdict(int)
        for num in nums:
            my_dict[num]+=1
        
        output=[]
        length=len(nums)      
        for key,value in my_dict.items():
            if value>length//3:
                output.append(key)
        return output
