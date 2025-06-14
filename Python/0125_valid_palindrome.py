# 125. Valid Palindrome
#
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1

            while right > left and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
            
        return True

    def alphaNum (self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))




    # The solution I came up with using regex (not optimized space-wise)
    def isPalindrome2(self, s: str) -> bool:
        
        lower_s = s.lower()
        new_s = re.sub(r'[^a-z0-9]', '', lower_s)

        # we create two poitners 
        right = len(new_s) - 1
        left = 0

        while left < right:
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True

    # Not optimal solution, since it uses extra memory
    def isPalindrome3(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]