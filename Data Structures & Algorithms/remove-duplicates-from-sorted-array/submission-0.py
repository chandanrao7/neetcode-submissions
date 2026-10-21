class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numset=sorted(set(nums))
        nums[:len(numset)]=numset
        return len(numset)

        