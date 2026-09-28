class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        time_stamps = self.time_map[key]
        l, r = 0, len(time_stamps) - 1
        prev_timestamp = time_stamps[0]
        while l <= r:
            m = l + (r - l) // 2
            if time_stamps[m][1] > timestamp:
                r -= 1
            elif time_stamps[m][1] < timestamp:
                prev_timestamp = time_stamps[m]
                l += 1
            else:
                return time_stamps[m][0]
        print(time_stamps)
        if prev_timestamp[1] > timestamp:
            return ""
        else:
            return prev_timestamp[0]

    # [1, 2, 3, 4, 6]