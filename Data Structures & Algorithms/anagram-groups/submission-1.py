class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ 
        We iterate over all strings in a list. 
        We know that they need to be the same length to be anagrams, so 
        we can check that first. Then we can see
        If length short, we just return
        """
        result = defaultdict(list)

        for s in strs:
            # initialize a space for each char in alphabet
            count  = [0] * 26

            for c in s:
                # For each char, we sub 'a' from it and then we increment 
                # that value on count
                value = ord(c) - ord('a')
                count[value] += 1
            # Once we loop the string, we add it to the list
            # with that array as the key (anagrams will have same array)
            result[tuple(count)].append(s)
        # At the end we return the values bc they hold the list of all the         
        # strings
        return list(result.values())

            