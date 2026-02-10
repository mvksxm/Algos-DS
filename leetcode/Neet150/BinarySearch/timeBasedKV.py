
# Time Complexity: O(log(n))
# Space Complexity: O(n*m), n -> keys, m -> versions


class TimeMap:

    def __init__(self):
        self._map = {}


    def _search_value(self, key, timestamp) -> str:

        if key not in self._map:
            return ""

        arr = self._map[key]
        l = 0
        r = len(arr) - 1
        idx = -1

        while l <= r:

            m = (l + r) // 2
            mid_val = arr[m]

            if mid_val[0] < timestamp:
                idx = m

            if mid_val[0] == timestamp:
                return mid_val[1]

            if mid_val[0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        if idx == -1:
            return ""

        return arr[idx][1]


    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self._map:
            self._map[key].append([timestamp, value])
            return

        self._map[key] = [[timestamp, value]]


    def get(self, key: str, timestamp: int) -> str:
        return self._search_value(key, timestamp)



if __name__ == "__main__":
    tm = TimeMap()
    tm.set("alice", "sad", 10)
    tm.set("alice", "happy", 20)
    tm.set("alice", "not happy", 30 )

    print(tm.get("alice", 35))
