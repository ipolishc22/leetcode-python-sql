# 1. Two Sum
# There is a brute force approach with O(n^2) time 
# Time complexity: O(n)
# Memory complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = nums[i] - target
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 