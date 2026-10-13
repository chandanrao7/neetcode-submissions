class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr1=[]
        for i in range(2):
            for num in nums:
                arr1.append(num)
        return arr1
        #return nums*2
        