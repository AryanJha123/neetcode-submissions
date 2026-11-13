class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        c = (l + r) // 2
        if len(nums) > 1:
            if nums[-1] > nums[0]:
                c = len(nums)
            else:
                while l < r:
                    if c > 0 and nums[c] < nums[c-1]:
                        break
                    else:
                        if nums[c] > nums[r]:
                            l = c + 1
                        else:
                            r = c - 1
                        c = (l + r) // 2
            rotation = c
        else:
            rotation = nums[0]
        if target < nums[0]:
            l = rotation
            r = len(nums) - 1
        else:
            r = rotation - 1
            l = 0
        c = (l + r) // 2
        while l <= r:
            if nums[c] == target:
                return c
            else:
                if target > nums[c]:
                    l = c + 1
                else:
                    r = c - 1
                c = (l + r) // 2
        return -1
        

