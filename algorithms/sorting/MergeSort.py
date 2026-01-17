# Merge Sort

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    left_arr = mergeSort(arr[:len(arr) // 2])
    right_arr = mergeSort(arr[len(arr) // 2:])

    return merging(left_arr, right_arr)


def merging(a, b):
    merged = []
    while a and b:
        if a[0] > b[0]:
            merged.append(b[0])
            b.pop(0)
        else:
            merged.append(a[0])
            a.pop(0)

    while a:
        merged.append(a[0])
        a.pop(0)

    while b:
        merged.append(b[0])
        b.pop(0)

    return merged


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


if __name__ == "__main__":
    arr = [6, 7, 3, 1, 2, 4]
    print(mergeSort(arr))
