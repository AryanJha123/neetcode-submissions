class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        outs = []
        for i in nums:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        for i in nums:
            d[i] -= 1
            for j in nums:
                if i == j and d[i] < 2:
                    break
                else:
                    d[j] -= 1
                    if d.get(-1*(i+j)) and d[-1*(i+j)] > 0:
                        temp = [i,j,(-1*(i+j))]
                        temp.sort()
                        outs.append(temp)
                    d[j] += 1
            d[i] += 1
        outs.sort()
        filtered = []
        for i in range(len(outs)):
            if outs[i] not in filtered:
                filtered.append(outs[i])
        return(filtered)