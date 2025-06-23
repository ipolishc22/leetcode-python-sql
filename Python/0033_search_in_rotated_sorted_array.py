# 33 Search in Rotated Sorted Array
#
# Time complexity: O(log n)
# Space complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1 


        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
                
            # left sorted portion
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1

            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1