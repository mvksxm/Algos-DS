from tester import Tester


# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach
# Create a window, where left boundary will be equal to the smallest value in the particular window and adjustable right
# boundary is always bigger than that smaller value. In case, if right boundary bumps into a value that smaller that the
# left boundary of a window - update the left boundary and set it to the recently discovered smaller value. Also, it's
# necessary to create a variable max_profit that will be holding a max profit, which can be earned. Value of a variable
# will be updated on each iteration of the right boundary by the result of max(max_profit, (right_boundary - left_boundary))

class Solution:
    def maxProfit(self, prices: list) -> int:

        if len(prices) <= 1:
            return 0

        l_border = 0
        r_border = 1

        max_profit = 0

        while r_border < len(prices):

            l_elem = prices[l_border]
            r_elem = prices[r_border]

            if r_elem <= l_elem:
                l_border = r_border
                r_border += 1
            else:
                profit = r_elem - l_elem
                max_profit = max(profit, max_profit)
                r_border += 1


        return max_profit


if __name__ == "__main__":
    sln = Solution()

    tst = Tester()
    test_cases = [
        [[[10,1,5,6,7,1]], 6],
        [[[10,8,7,5,2]], 0]
    ]

    tst.array_test(test_cases, sln.maxProfit)



