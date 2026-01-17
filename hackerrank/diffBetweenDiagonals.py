# Simple problem
def differenceBetweenDiagonals(inpt):
    diag_one = 0
    diag_two = 0

    for i in range(len(inpt)):
        diag_one += inpt[i][i]
        diag_two += inpt[i][len(inpt) - 1 - i]

    diff = diag_one - diag_two
    return abs(diff)


def stairCase(n):
    for i in range(n):
        print(" " * (n - 1 - i), "#" * (i + 1))


def breakingTheRecord(arr):
    output_arr = [0, 0]
    prev_min = arr[0]
    prev_max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > prev_max:
            output_arr[0] += 1
            prev_max = arr[i]
        if arr[i] < prev_min:
            output_arr[1] += 1
            prev_min = arr[i]

    return output_arr


# def divisibleSumPairs(arr, n):
#     hashMap = {}
#     cnt = 0
#
#     def supportFunc(trg, ind):
#         for j in hashMap[target_val]:
#             if hashMap[target_val][j] < ind:
#                 return True
#
#         return False
#
#     for i in range(len(arr)):
#         if arr[i] not in hashMap:
#             hashMap[arr[i]] = [i]
#
#         if arr[i] in hashMap:
#             hashMap[arr[i]].append(i)
#
#         target_val = n - arr[i]
#         if target_val in hashMap and supportFunc(target_val, i):
#             cnt += 1
#
#     return cnt


def divisibleArray(arr, n):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % n == 0:
                cnt += 1
    return cnt


if __name__ == "__main__":
    sample_input1 = [[1, 2, 3],
                     [5, 7, 4],
                     [3, 6, 2]]

    sample_input2 = [[1, 2, 3, 4],
                     [5, 7, 4, 6],
                     [3, 6, 2, 8],
                     [3, 6, 2, 8]]

    # print(differenceBetweenDiagonals(sample_input1))
    # print(differenceBetweenDiagonals(sample_input2))

    # stairCase(4)
    # print(breakingTheRecord([10, 5, 20, 20, 4, 5, 2, 25, 1]))
    # print(breakingTheRecord([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))

    print(divisibleArray([1, 3, 2, 6, 1, 2], 3))
