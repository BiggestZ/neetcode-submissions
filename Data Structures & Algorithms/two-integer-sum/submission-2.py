class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We take each num sub from target and see if it is in the map
        tracker = {}
        for i, num in enumerate(nums):
            temp = target - num
            # if the diff is found in the map
            if temp in tracker:
                return [tracker[temp], i]
            else:
                # Store the new variables
                tracker[num] = i
            