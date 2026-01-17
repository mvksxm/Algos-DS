# Supposed to be a sliding windo
class Solution:
    def maxProfit(prices: list) -> int:
        # if not prices:
        #     return 0
        #
        # if len(prices) == 1:
        #     return 0
        #
        # lft_pointer = 0
        # right_pointer = lft_pointer + 1
        #
        # profit = 0
        # while (right_pointer > lft_pointer and right_pointer < len(prices)):
        #     profit = max(profit, prices[right_pointer] - prices[lft_pointer])
        #
        #     curr_left = lft_pointer
        #     curr_right = right_pointer
        #
        #     for i in range(lft_pointer+1, len(prices)):
        #         if prices[i] < prices[lft_pointer]:
        #             lft_pointer = i
        #             right_pointer = lft_pointer + 1 if right_pointer < lft_pointer else right_pointer
        #             break
        #
        #     for i in range(right_pointer+1, len(prices)):
        #         if prices[i] >= prices[right_pointer]:
        #             right_pointer = i
        #             break
        #
        #     if lft_pointer == curr_left and right_pointer == curr_right:
        #         break
        #
        # return profit
        # ===================================
        # if not prices or len(prices) == 1:
        #     return 0
        #
        # l_p = 0
        # r_p = len(prices) - 1
        #
        # mx_val = 0
        # min_val = 100
        #
        # while l_p <= r_p:
        #     mx_val = max(mx_val, prices[r_p])
        #     min_val = min(min_val, prices[l_p])
        #     l_p += 1
        #     r_p -= 1
        #
        # diff = mx_val - min_val
        # return diff if diff > 0 else 0
        # ======================================

        if not prices or len(prices) == 1:
            return 0

        l_p = 0
        r_p = l_p + 1

        diff = 0

        while r_p < len(prices):
            if prices[l_p] >= prices[r_p]:
                l_p = r_p
                r_p += 1
            elif prices[l_p] < prices[r_p]:
                diff = max(diff, prices[r_p] - prices[l_p])
                r_p += 1

        return diff



print(Solution.maxProfit([7,1,5,3,6,4]))