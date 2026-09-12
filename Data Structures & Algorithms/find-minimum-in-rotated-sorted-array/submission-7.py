class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If the array is in sorted order, we can return 
        # First element
        l, r = 0, len(nums)-1
        low=nums[l]

        while l <= r:
            # if true: list in sorted order
            if nums[l] <= nums[r]:
                low = min(low, nums[l])
                break
            # If false list has 2 sorted sections. We do BS to 
            # find mid and see if it is in 1st or 2nd sorted 
            # section.
            mid = (l + r) // 2
            low = min(low, nums[mid])
            # If the middle is greater, it is in ascending 
            # order, so we are in the "bigger" sorted section
            # Bc we want the min, we would want to move right.
            if nums[mid] >= nums[l]:
                l = mid+1
            # If false, then we are already in the small 
            # section and want to search to the left
            else:
                r = mid-1
        return low