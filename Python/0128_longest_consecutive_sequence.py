# 128. Longest Consecutice Sequence
#
# Time complexity: O(n)
# Memory complexity: O(n) since we had to create a set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # checking whether n is the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length+=1
                longest = max(length, longest)
        return longest 