class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calc_area(l, r):
            width = r - l
            height = min(heights[l], heights[r])
            return height * width
        
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            current_area = calc_area(l, r)
            if current_area > max_area:
                max_area = current_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
