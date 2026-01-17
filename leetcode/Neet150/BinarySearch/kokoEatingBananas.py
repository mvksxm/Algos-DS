import math

class Solution:
    def minEatingSpeed(piles: list, h: int) -> int:


        possible_rates = range(1, max(piles) + 1)
        l_p = 0
        r_p = len(possible_rates) - 1
        possible_solution = 1000**3 + 1

        total_hours = 0

        while l_p <= r_p:
            mid_index = l_p + ((r_p - l_p) // 2)
            mid_elem = possible_rates[mid_index]

            for p in piles:
                total_hours += math.ceil(p / mid_elem)

            # if total_hours == h:
            #     return mid_elem

            if total_hours <= h:
                r_p = mid_index - 1
                possible_solution = min(possible_solution, mid_elem)
            elif total_hours > h:
                l_p = mid_index + 1

            total_hours = 0

        return possible_solution


print(Solution.minEatingSpeed([1,4,3,2], 9))
print(Solution.minEatingSpeed([25,10,23,4], 4))
print(Solution.minEatingSpeed([30,11,23,4,20], 6))
print(Solution.minEatingSpeed([312884470], 312884469))