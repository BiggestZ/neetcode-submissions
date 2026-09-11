class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = math.inf
        l, r = 0, len(nums)-1

        while l <=r:
            low = min(low, nums[l], nums[r])
            l += 1
            r -= 1
        return low
