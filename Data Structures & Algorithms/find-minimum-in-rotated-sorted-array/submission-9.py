class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Set starter vars.
        hi, lo = len(nums)-1, 0
        min = nums[lo]

        # Check if it is in order
        if nums[lo] < nums[hi]:
            return min

        while lo < hi:
            
            mid = (lo + hi) // 2

            if nums[mid] < min:
                 min = nums[mid]
            
            # If the mid > hi, we are in the larger sorted half, so we go right
            if nums[mid] > nums[hi]:
                lo = mid + 1
            # Else, mid < hi means we are in the smaller half, so we bring the hi down
            else:
                hi = mid
        return nums[lo]
                
                