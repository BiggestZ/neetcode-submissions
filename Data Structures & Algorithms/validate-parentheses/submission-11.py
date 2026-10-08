class Solution:
    def isValid(self, s: str) -> bool:
        """Concept:
        We want to create a list that we append to with the opening symbols. 
        Each time a closing symbol comes up, we check the top of the list, and if that matching symbol is
        there we pop, if not we return false
        We return True at the very end after completing the loop
        """

        tracker = []

        if not s or len(s) < 2:
            return False

        # Build map
        closeToOpen = {
            "}": "{", 
            "]": "[", 
            ")": "("
        }

        # Now we loop thru each character in the string
        for c in s:
            # if it is in the map, we look for its match and pop
            if c in closeToOpen:
                # Check if the end element does NOT match(It would be the most recently appended)
                # NOTE: Check if tracker is empty before attempting to access it, or will throw out of bounds
                if not tracker or tracker[-1] != closeToOpen[c]:
                    return False
                tracker.pop()
            else:
                # If the character is not a close, we just append it
                tracker.append(c)
                    
        # If we complete the loop, return True
        # NOTE: We return `not tracker` so that if the list is not empty, we know it did not complete
        return not tracker
            
                

        