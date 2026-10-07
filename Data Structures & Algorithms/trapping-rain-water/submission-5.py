class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]

        res = 0

        while l < r:
            print(maxL, maxR)
            if maxL < maxR:
                l += 1
                print("left")
                maxL = max(maxL, height[l])
                print(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                print("right")
                maxR = max(maxR, height[r])
                print(maxR, height[r])
                res += maxR - height[r]
        
        return res