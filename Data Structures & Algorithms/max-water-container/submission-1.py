class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We create pointers at either end of the graph
        l, r = 0, len(heights)-1
        water = -1

        # Not '<=' bc we can't have them be the same wall
        while l < r:
            # The height is determined by the smaller of the 2
            # the base is the difference in indicies
            height = min(heights[l], heights[r])
            base = r - l
            product = base * height
            water = max(water, product)
            # How do we determine which pointer to move and how much?
            # Idea: We move from the smallest height between the 2
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return water