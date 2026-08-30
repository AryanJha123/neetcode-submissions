class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seqlen = [1]
        started = False
        d = set()
        for n in nums:
            d.add(n)
        for n in nums:
            if n-1 not in d:
                seqstart = n
                seqlen.append(0)
                started = True
            if started:
                while seqstart in d:
                    seqlen[-1] += 1
                    d.remove(seqstart)
                    seqstart += 1
        return max(seqlen)