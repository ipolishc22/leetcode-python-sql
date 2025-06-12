# 49. Group Anagrams
# If using sorting the time complexity would be O(mnlogn)
# Time complexity: O(mn) where m is a number of strings we are given and n is the average sength of a string
# Space complexity: O(mn)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 # a ... z 
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return  list(res.values())
