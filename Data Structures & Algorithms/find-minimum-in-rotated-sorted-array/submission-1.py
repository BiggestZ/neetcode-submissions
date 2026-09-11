class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = math.inf
        l, r = 0, len(nums)-1

        while l <=r:
            if nums[l] < nums[r]:
                low = min(nums[l], low)
                break
            
            m = (l+r) // 2
            low = min(low, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return low
