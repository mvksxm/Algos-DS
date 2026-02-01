from typing import List
from tester import Tester

# Time Complexity: O(log(n)*n) + O(n^2) + O(n) = O(n^2)
# Space Complexity: res_set - O(n), if res does not count - then O(1)

# Approach
# First of all - sort the array in ascending order.
# Then iterate through the array by using two loops for and inner while. For will be responsible for the root_pointer, inner
# while for the left pointer and right pointer in the sub array, whose first index equals to the root_pointer+1. On each
# iteration of the inner while loop, sum = root_pointer elem + left_pointer elem + right_pointer elem. In case, if sum equals
# to 0 -> append to the res_set in a form of a tuple, otherwise, in case if sum < 0 -> move the left pointer and if sum > 0
# move right pointer. After main iteration -> iterate through res set, create a list of lists from it and return.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res_set = set()
        nums.sort()


        for i in range(len(nums)-2):
            root_num = nums[i]
            l_p = i + 1
            r_p = len(nums)-1

            while l_p < r_p:
                l_num = nums[l_p]
                r_num = nums[r_p]

                sm = root_num + l_num + r_num

                if sm == 0:
                    combined_tuple = (root_num, l_num, r_num)
                    res_set.add(combined_tuple)

                    l_p += 1
                    r_p -= 1
                elif sm < 0:
                    l_p += 1
                else:
                    r_p -= 1

        return [list(res) for res in res_set]


if __name__ == "__main__":
    sl = Solution()

    # [-4, -1, -1, 0, 1, 2]
    # [-4, -4, 0, 2, 2]

    print(sl.threeSum([-1,0,1,2,-1,-4]))
    print(sl.threeSum([-4, -4, 0, 2, 2]))
