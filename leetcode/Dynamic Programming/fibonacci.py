# Recursive, Iteration Solution, Recursive with Memoization


def fibRecursive(n):
    if n == 1 or n == 2:
        return 1

    return fibRecursive(n - 1) + fibRecursive(n - 2)


mem_arr = [None] * 7


# Memoization
def fibMemoization(n=7):
    # 1 1 2 3 5 8
    if mem_arr[n - 1]:
        return mem_arr[n - 1]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibMemoization(n - 1) + fibMemoization(n - 2)
    mem_arr[n - 1] = result
    return result


# Default Solution
def simpleFibonacci(n):
    a = [1, 1]

    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])

    return a[-1]


if __name__ == "__main__":
    n = 8
    # 1 1 2 3 5 8 13
    print(simpleFibonacci(n))
