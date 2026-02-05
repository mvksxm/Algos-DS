from typing import List

from tester import Tester


# Time Complexity: n*log(n)
# Space Complexity: O(n)

# Approach
# Create an array that would contain positions in a form of the tuple -> (original idx, position). Sort that array.
# Sorting is needed in order to iterate through the array from the biggest position to the lowest one. Also, original
# indexes need to be present in tuples, so that the respective speed could be accessed from speed array.
# Iterate through the sorted array. On each iteration calculate the curr_time_to_dest, which represents the amount of time
# that needs to be spent to arrive to dest from pos with the provided speed. In case, if curr_time_to_dest is bigger
# than the time_to_dest (by now the biggest time to dest), we can assume that car from the current position with its
# given speed will not be a part of the fleet before it, so we can increase the fleet count and update the time_to_dest
# with the bigger curr_time_to_dest.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        indexed_position = [(i, position[i]) for i in range(len(position))]
        sorted_position = sorted(indexed_position, key=lambda x: x[1])

        time_to_dest = 0
        fleet_count = 0

        for i in range(len(sorted_position) - 1, -1, -1):

            curr_pos = sorted_position[i]
            curr_time_to_dest = (target - curr_pos[1]) / speed[curr_pos[0]]

            if curr_time_to_dest > time_to_dest:
                fleet_count += 1
                time_to_dest = curr_time_to_dest

        return fleet_count

if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_cases = [
        [[10, [1,4], [3,2]], 1],
        [[10, [4,1,0,7], [2,2,1,1]], 3]
    ]

    tst.array_test(test_cases, sln.carFleet)
