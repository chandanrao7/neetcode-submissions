class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Solution 1  Array
        # t=s.copy()
        # length=len(s)
        # j=0
        # for i in range(length-1,-1,-1):
        #     s[j]=t[i]
        #     j=j+1
        # Solution 2  In-built
        # s.reverse()
        #Solution 3  Stack
        # stack=[]
        # for c in s:
        #     stack.append(c)
        
        # i=0
        # while stack:
        #     s[i]=stack.pop()
        #     i=i+1
        # SOlution 4:
        l=0
        r=len(s)-1

        while(l<r):
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1