def quickSort(seq):
    if len(seq) <= 1:
        return seq

    pivot = seq.pop()
    elements_bigger = []
    elements_smaller = []

    for elem in seq:
        if elem > pivot:
            elements_bigger.append(elem)
        else:
            elements_smaller.append(elem)

    # Recursive call explained bellow
    return quickSort(elements_smaller) + [pivot] + quickSort(elements_bigger)


if __name__ == "__main__":
    seq = [4, 3, 1, 10, 11, 6]
    print(quickSort(seq))

# Quick Sort
# [4,3,1, 10, 11, 6]

# Iteration 1  Complexity O(n*log(n))
# [4, 3, 1] + [6] + [10, 11]
#   /  \              / \
# [1] + [4, 3]     [10] [11]
#        /  \
#      [3] [4]
