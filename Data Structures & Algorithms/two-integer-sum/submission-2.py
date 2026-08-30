class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in indices and indices[target-nums[i]] != i:
                return [i, indices[target-nums[i]]]