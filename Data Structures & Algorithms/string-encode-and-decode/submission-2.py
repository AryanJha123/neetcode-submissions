class Solution:

    def encode(self, strs: List[str]) -> str:
        b = ''
        for j in strs:
            b += str(len(j))
            b += '#'
            b += j
        return b
    def decode(self, s: str) -> List[str]:
        r = []
        ptr = 0
        while ptr < len(s):
            l = int(s[ptr:(s[ptr:].index('#')+ptr)])
            dig = len(str(l))
            r.append(s[ptr+dig+1:ptr+l+dig+1])
            ptr += l + dig+1
        return r