# 153 Find Minimum in Rotated Sorted Array 
#
# Time complexity: O(log n) since we use binary search
# Space complexity: O(1) since we don't create any new data structures
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]: 
                right = mid - 1

        return res