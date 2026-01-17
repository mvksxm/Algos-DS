
class Solution:
    def maxArea(heights: list) -> int:
        mx = 0
         # [3, 7, 1, 9, 4, 2, 8, 5]
        lft_p = 0
        right_p = len(heights) - 1

        while lft_p < right_p:
            min_element = min(heights[lft_p], heights[right_p])
            mx = max(mx, min_element*(right_p - lft_p))

            if heights[lft_p] > heights[right_p]:
                right_p -= 1
            else:
                lft_p += 1

        return mx

print(Solution.maxArea([2,2,2]))



