# Solution 1 (using hash maps)
# Time complexity: O(n)
# Memory complexity: O(n)
# Downside: We need more memory 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
    

# Solution 2 (using sorting)
# Time complexity: O(nlogn) if the algorithm is good
# Memory complexity:  O(1) can be assumed
# Downside: sorting might take extra memory. Not as efficient as the first solution
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)