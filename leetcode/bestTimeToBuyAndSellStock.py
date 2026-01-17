
# O(n)
def maxProfit(arr):
    max_profit = 0  # 4 # 5
    buy_index = 0
    # arr1 = [7,1,5,3,6,4]
    for i in range(1, len(arr)):
        max_profit = max(max_profit, arr[i] - arr[buy_index])

        if arr[i] < arr[buy_index]:
            buy_index = i

    return max_profit


if __name__ == "__main__":
    arr1 = [7, 1, 5, 3, 6, 4]
    arr2 = [7, 6, 4, 3, 1]

    print(maxProfit(arr2))
    hashMap = {3:0, 1:0}