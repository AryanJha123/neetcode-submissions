class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            x = ''.join(sorted(i))
            if d.get(x) == None:
                d[x] = (i, )
            else:
                d[x] += (i, )
        out = []
        for j in list(d.keys()):
            t = []
            for k in d[j]:
                t.append(k)
            out.append(t)
        return out