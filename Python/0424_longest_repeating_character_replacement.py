# 424. Longest Repeating Character Replacement
#
# Time complexity: O(n)
# Space complexity: O(m)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        maxf = 0 # maximum frequency variable 

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res

