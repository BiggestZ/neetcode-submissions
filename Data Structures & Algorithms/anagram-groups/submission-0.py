class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # We iterate over all strings in a list. 
    # We know that they need to be the same length to be anagrams, so we can check that first. Then we can see
        # If length short, we just return
        if len(strs) <= 1:
            return [strs]

        anagrams = defaultdict(list)
        # Iterate through list
        for i in strs:
            count = [0]*26 # mimics alphabet [a-z]
            for c in i:
                #Now we compare asciis
                count[ord(c) - ord('a')] += 1
            #Group all strings with the same count
            # We use tuple bc lists are mutable so it could change and dict keys cannot so we move it to tuple
            anagrams[tuple(count)].append(i)
        return list(anagrams.values())
            