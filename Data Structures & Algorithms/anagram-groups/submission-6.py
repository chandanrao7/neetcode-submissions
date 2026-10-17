class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            res_sorted=''.join(sorted(s))
            res[res_sorted].append(s)
        return list(res.values())



        

# strs = ["act","cat"]
#  'c','a','t' ->"act"
# res[act]=["act","cat"]
# {act:["act","cat"]}