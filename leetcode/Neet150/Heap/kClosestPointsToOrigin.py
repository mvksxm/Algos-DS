import math
import heapq

class Solution:
    def kClosest(points: list, k: int) -> list:

        if not points:
            return []

        hm = {}
        heap = []
        result = []

        for point in points:
            diff = math.sqrt((0-point[0])**2 + (0-point[1])**2)
            heap.append(diff)

            if diff in hm:
                hm[diff].append(point)
            else:
                hm[diff] = [point]


        heapq.heapify(heap)

        for i in range(k):
            heap_elem = heapq.heappop(heap)
            result.append(hm[heap_elem].pop())

        return result

if __name__ == "__main__":
    points = [[0,2],[2,0],[2,2]]
    k = 2
    print(Solution.kClosest(points, k))