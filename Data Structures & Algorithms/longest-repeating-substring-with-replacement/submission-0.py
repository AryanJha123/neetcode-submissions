class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        di = {}
        l = 0
        r = 0
        maxlen = 0
        while r < len(s):
            if di.get(s[r]):
                di[s[r]] += 1
            else:
                di[s[r]] = 1
            while sum(list(di.values())) - max(list(di.values())) > k and l < r:
                di[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen