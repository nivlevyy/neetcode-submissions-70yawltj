class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum=0
        if not heights:
            return maximum

        l=0
        r=len(heights)-1
        
        while(l<r):
            if maximum<min(heights[l],heights[r])*(r-l):
                maximum=min(heights[l],heights[r])*(r-l)
            if heights[l]<=heights[r]:
                l+=1
            else:
               r-=1

        return maximum
            