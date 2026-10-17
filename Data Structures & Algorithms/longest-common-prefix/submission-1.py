class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if len(s)==i or s[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]






        
#["bat","bag","bank","band"]
#length=3
# i=0, 1 2 
#i=0 and s='bat'
# s=bag and i=2