class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        c = (l + r) // 2
        if len(nums) > 1:
            while l < r:
                if nums[c] < nums[c-1]:
                    return nums[c]
                else:
                    if nums[c] > nums[r]:
                        l = c + 1
                    else:
                        r = c - 1
                    c = (l + r) // 2
            return nums[c]
        else:
            return nums[0]