class Solution:
    def findMin(self, nums: List[int]) -> int:
        c = (len(nums)-1)//2
        r = len(nums)-1
        l = 0
        solved = False
        final = nums[-1]
        if len(nums) == 1:
            return nums[0]
        while l <= r:
            c = l + (r-l)//2
            if nums[c] < nums[c-1]:
                return nums[c]
            elif nums[c] > nums[r]:
                l = c + 1
            else:
                r = c - 1