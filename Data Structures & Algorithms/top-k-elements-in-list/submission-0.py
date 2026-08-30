class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if d.get(i) == None:
                d[i] = 1
            else:
                d[i] += 1
        s = []
        for j in list(d.keys()):
            s.append((d[j], j))
        s.sort(reverse=True)
        a = []
        for i in range(k):
            a.append(s[i][1])
        return a