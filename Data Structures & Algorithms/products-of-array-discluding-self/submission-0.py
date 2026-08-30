class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
                post[i] = 1
            else:
                pre[i] = pre[i-1]*nums[i-1]
                post[len(nums)-1-i] = post[len(nums)-i] * nums[len(nums)-i]
        total = [0]*len(nums)
        for i in range(len(nums)):
            total[i] = pre[i] * post[i]
        return total