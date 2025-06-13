# 238. Product of Array Except Self 
#
# Time complexity: O(n)
# Space complexity: O(n) for the output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # create the result array

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res