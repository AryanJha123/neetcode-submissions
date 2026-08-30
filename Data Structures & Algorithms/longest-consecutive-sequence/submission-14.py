class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seqlen = [1]
        started = False
        d = {}
        for n in nums:
            d[n] = 1
        for n in nums:
            if not d.get(n-1):
                seqstart = n
                seqlen.append(0)
                started = True
            if started:
                while d.get(seqstart):
                    seqlen[-1] += 1
                    del d[seqstart]
                    seqstart += 1
        return max(seqlen)