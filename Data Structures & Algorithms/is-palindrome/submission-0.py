class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1 # Set pointers on either side
        while l < r:
            # These functions serve to skip non-alphanumerical chars
            while l < r and not self.isAlphaNum(s[l]):
                print('left')
                l+=1
            while r > l and not self.isAlphaNum(s[r]):
                print('Right')
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))