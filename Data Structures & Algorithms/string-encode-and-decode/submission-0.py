class Solution:

    def encode(self, strs: List[str]) -> str:
        b = ''
        for j in strs:
            b += j
            b += 'é'
        return b
    def decode(self, s: str) -> List[str]:
        r = []
        r = s.split('é')
        return r[:-1]