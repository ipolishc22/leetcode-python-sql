# 11. Container With Most Water
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            water = (right-left) * min(heights[left], heights[right])
            result = max(result, water)

            if heights[left] >= heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1

        return result