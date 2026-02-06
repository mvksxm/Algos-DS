from tester import Tester

# Time Complexity: O(n*log(m))
# Space Complexity: O(1)

# Approach
# By using Binary Search, continuously divide max value of the piles array by two (in order to find the medium speed).
# On each division, calculate the amount of time that would be needed for eating all the piles with the medium speed.
# In case, if amount of time is smaller than h, let right pointer of Binary Search be equal to medium_speed - 1, so that
# it was possible to get the smaller speed that could produce a bigger time respectively (closer to h). On the other hand,
# in case, if medium speed is bigger than h, let the left pointer of Binary Search window be equal to the medium_speed + 1,
# in order to produce a higher speed during the next division, which, in turn, would produce a smaller amount of hours.

class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:

        r_speed = max(piles)
        l_speed = 1

        curr_min_speed = r_speed

        while l_speed <= r_speed:
            middle_speed = l_speed + ((r_speed - l_speed) // 2)

            hours = 0
            for pile in piles:
                hours += pile // middle_speed
                if pile % middle_speed > 0:
                    hours += 1

            if hours <= h:
                curr_min_speed = middle_speed
                r_speed =  middle_speed - 1
            else:
                l_speed = middle_speed + 1

        return curr_min_speed


if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_cases = [
         [[[1,4,3,2],9], 2],
         [[[25,10,23,4], 4], 25]
    ]

    tst.array_test(test_cases, sln.minEatingSpeed)