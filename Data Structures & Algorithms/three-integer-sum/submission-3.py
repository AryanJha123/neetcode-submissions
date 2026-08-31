class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        r = len(nums)-1
        out = []
        for index, num in enumerate(nums):
            while r > l:
                if l == index:
                    l += 1
                elif r == index:
                    r -= 1
                elif nums[l] + nums[r] > -1*num:
                    r -= 1
                elif nums[l] + nums[r] < -1*num:
                    l += 1
                else:
                    temp = [nums[l], nums[r], num]
                    temp.sort()
                    if temp not in out:
                        out.append(temp)
                    l += 1
            l = 0
            r = len(nums)-1
        return out