class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        original = str(x)
        reversed = original[::-1]
        return original == reversed
        
        