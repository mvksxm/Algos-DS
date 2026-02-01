# Quick Sort

# Example array - [4,3,1, 10, 11, 6]

# Average complexity - O(log(n)*n)
# Worst complexity - O(n^2)

# Iteration 1 (Pivot - 6, arr[len(arr)-1])
# [4, 3, 1] + [6] + [10, 11]
#   /  \              / \
# [1] + [4, 3]     [10] [11]
#        /  \
#      [3] [4]

# Iteration 2 (Pivot - 4, arr[0])
# [3, 1] + [4] + [10, 11, 6]
#  /  \            /  |   \
# [1] [3]        [6] [10] [11]

def quick_sort(arr: list):

    if not arr:
        return []

    pivot_idx = 0
    pivot = arr[pivot_idx]

    arr_smaller = [arr[i] for i in range(len(arr)) if arr[i] <= pivot and i != pivot_idx]
    arr_bigger = [elem for elem in arr if elem > pivot]

    return quick_sort(arr_smaller) + [pivot] + quick_sort(arr_bigger)


if __name__ == "__main__":
    arr = [4,4, 3,1, 10, 11, 6]
    print(quick_sort(arr))

# pivot - 4
# [3, 1] + [4] + [10, 11, 6]
# [3,1] - [1] + [3] + [] - [1,3]
# [10, 11, 6] -  [6]([] + [6] + []) + [10]([] + [10] + []) + [11]([] + [11] + [])