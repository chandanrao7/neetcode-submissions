class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution 1
        # s=sorted(s)
        # t=sorted(t)
        # if s==t:
        #     return True
        # return False
        #Solution 2
        # if len(s)!=len(t):
        #     return False
        # return sorted(s)==sorted(t)
        #Solution 3
        a=Counter(s)
        print(a)
        return Counter(s)==Counter(t)