class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = []
        for i in nums:
            targets.append(target-i)
        targets.sort()
        b = nums.copy()
        b.sort()
        i = 0
        point = 0
        g = []
        while i < len(targets) and point < len(b):
            if b[point] == targets[i]:
                g = [b[point], -1 * targets[i] + target] 
                if g[0] == g[1]:
                    x = nums.index(g[0])
                    nums.remove(g[0])
                    o = [x, nums.index(g[1])+1]
                else:
                    o = [nums.index(g[1]), nums.index(g[0])]
                    o.sort()
                return o
            elif b[point] < targets[i]:
                point += 1
            else:
                i += 1