class TimeMap:

    def __init__(self):
        self.value_dict = defaultdict(list)
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[key].append(value)
        self.time_dict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.time_dict.get(key, []))-1
        #Binary Search
        while l <= r:
            mid = (l + r) // 2
            curr_ts = self.time_dict[key][mid]
            if curr_ts == timestamp:
                # Auto-sorted bc monotonically inc.
                return self.value_dict[key][mid]
            elif curr_ts > timestamp:
                r = mid -1
            else:
                l = mid + 1
        return self.value_dict[key][r] if r >= 0 else ""