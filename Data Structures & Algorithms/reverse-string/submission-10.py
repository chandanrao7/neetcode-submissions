class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t=s.copy()
        length=len(s)
        j=0
        for i in range(length-1,-1,-1):
            s[j]=t[i]
            j=j+1
        