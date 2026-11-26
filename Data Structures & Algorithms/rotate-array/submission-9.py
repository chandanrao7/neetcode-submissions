class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution 1
        # l=0
        # k=k%len(nums)
        # r=len(nums)-1
        # while l<r:
        #     nums[l], nums[r]=nums[r], nums[l]
        #     l+=1
        #     r-=1        
        # l=0
        # r=k-1
        # while l<r:
        #     nums[l], nums[r]=nums[r], nums[l]
        #     l+=1
        #     r-=1      
        # l=k
        # r=len(nums)-1          
        # while l<r:
        #     nums[l], nums[r]=nums[r], nums[l]
        #     l+=1
        #     r-=1
        
        #Solution 2
        
        n=len(nums)
        k=k%n
        while k:
            temp=nums[-1]
            for i in range(n-1, 0, -1):
                nums[i]=nums[i-1]
            nums[0]=temp
            k-=1

        # 1 2 3 4 5 6 7 8

        