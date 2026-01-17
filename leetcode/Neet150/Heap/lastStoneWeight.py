from heapq import heapify

from SortingAlgos.QuickSort import quickSort
import heapq

class Solution:
    def lastStoneWeightBruteForce(stones: list) -> int:

        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]

        sorted_stones = quickSort(stones)

        i = len(sorted_stones) - 2
        while i >= 0:
            diff = sorted_stones[i+1] - sorted_stones[i]

            if diff > 0:
                sorted_stones.pop(i+1)
                sorted_stones[i] = diff
                i -= 1
                sorted_stones = quickSort(sorted_stones)
            elif diff == 0:
                sorted_stones.pop(i+1)
                sorted_stones.pop(i)
                i -= 2

        return sorted_stones[0]

    def lastStoneWeightOptimal(stones: list) -> int:

        if not stones:
            return 0

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        for _ in range(len(stones)):
            max_elem = heapq.heappop(stones)

            if not stones:
                return -max_elem

            max_elem2 = heapq.heappop(stones)

            diff = -max_elem - -max_elem2
            heapq.heappush(stones, -diff)



    def quickSort(self, arr: list) -> list:
        if len(arr) <= 1:
            return arr

        elements_less = []
        elements_higher = []

        pivot = arr.pop()

        for elem in arr:
            if elem > pivot:
                elements_higher.append(elem)
            else:
                elements_less.append(elem)


        return quickSort(elements_less) + [pivot] + quickSort(elements_higher)

if __name__ == "__main__":
    test_arr = [2,3,6,2,4]
    print(Solution.lastStoneWeightOptimal(test_arr))