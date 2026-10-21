class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:]=nums1[:m]
        # nums2[:]=nums2[:n]
        # for num in nums2:
        #     nums1.append(num)
        # nums1.sort()
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()