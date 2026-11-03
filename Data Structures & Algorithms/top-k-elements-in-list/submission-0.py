class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We do a bucketsort and counter 
        bucket = [[] for _ in range(len(nums)+1)] # lenght of the list
        counter = {}
        result = []
        # We will loop and store them in the counter {value: count}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1 # starts at 0 if value not there
        
        # Now we loop each element in the dictionary and insert it in 'bucket' at index 'value'
        for num, count in counter.items():
            bucket[count].append(num)   # {1: 3} -> [, , [1], ] 
        
        # Now we iterate in reverse and get the elements staarting from the back until k = 0
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                k-=1
                if k == 0:
                    return result