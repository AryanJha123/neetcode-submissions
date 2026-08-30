class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = []
        v = []
        for i in s:
            u.append(i)
        for i in t:
            v.append(i)
        u.sort()
        v.sort()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if u[i] != v[i]:
                return False
        return True