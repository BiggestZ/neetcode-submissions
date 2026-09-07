class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Need to be same length
        if(len(s) != len(t)):
            return False;
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # This will update the element by +1
            # We use get because it lets us use default value of 0
        for c in countS:
            if countS[c] != countT.get(c,0): # Checks the key (# of occurrences)
                return False
        return True