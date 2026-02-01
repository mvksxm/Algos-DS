from tester import Tester

# Merge Sort
# Time Complexity: O(log(n)*n)

# [6, 7, 3, 1 ,2, 4]
#     /   \                                 merged = []
# [6, 7, 3] [1, 2, 4]    -> merging         while a and b:
#     /  \                                     if a[0] > b[0]:
#   [6]  [7, 3]  3,7,6                                 merged.append(b[0])
#          / \                                    b.pop(0)
#       [7]   [3]                              else:
#                                                 merged.append(a[0])
#                                                 a.pop(0)
#

def _merge_arrays(left_arr, right_arr):
    merged_arr = []
    l_p = 0
    r_p = 0

    while l_p < len(left_arr) and r_p < len(right_arr):
        left_elem = left_arr[l_p]
        right_elem = right_arr[r_p]

        if left_elem > right_elem:
            merged_arr.append(right_elem)
            r_p += 1
        elif right_elem > left_elem:
            merged_arr.append(left_elem)
            l_p += 1
        else:
            merged_arr += [left_elem, right_elem]
            r_p += 1
            l_p += 1

    if l_p != len(left_arr):
        merged_arr += left_arr[l_p:len(left_arr)]

    if r_p != len(right_arr):
        merged_arr += right_arr[r_p:len(right_arr)]

    return merged_arr


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle_idx = len(arr) // 2
    left_arr = arr[:middle_idx]
    right_arr = arr[middle_idx:]

    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    return _merge_arrays(left_sorted, right_sorted)

if __name__ == "__main__":
    tst = Tester()

    test_cases = [
        [[[6, 7, 3, 1, 2, 4]], [1, 2, 3, 4, 6, 7]],
        [[[3, 3, 1, 1]], [1, 1, 3, 3]]
    ]

    tst.array_test(test_cases, merge_sort)
