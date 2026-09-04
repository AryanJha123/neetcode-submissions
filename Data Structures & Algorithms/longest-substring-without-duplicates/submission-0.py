class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        r = 0
        maxlen = 0
        while r < len(s):
            if s[r] not in charset:
                charset.add(s[r])
                maxlen = max(maxlen, r-l+1)
            else:
                while s[l] != s[r]:
                    charset.remove(s[l])
                    l += 1
                charset.remove(s[l])
                l += 1
                charset.add(s[r])
            r += 1
        return maxlen
