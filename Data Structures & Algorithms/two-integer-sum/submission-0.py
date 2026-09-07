class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i in range(len(nums)):
            goal = target - nums[i] 
            if goal in sum:
                return [sum[goal], i]
            sum[nums[i]] = i
        return -1
            
            