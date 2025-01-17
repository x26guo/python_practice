class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((value, timestamp))
        else:
            self.dic[key] = [(value, timestamp)]


    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key in self.dic:
            start = 0
            end = len(self.dic[key]) - 1
            while start <= end:
                mid = start + (end - start) // 2
                time = self.dic[key][mid][1]
                if time == timestamp:
                    return self.dic[key][mid][0]
                elif time > timestamp:
                    end = mid - 1
                else:
                    start = mid + 1
                    result = self.dic[key][mid][0]

        return result

time_map = TimeMap()
time_map.set("foo", "bar", 1)
print(time_map.get("foo", 1))
print(time_map.get("foo", 3))
time_map.set("foo", "bar2", 4)
print(time_map.get("foo", 4))
print(time_map.get("foo", 5))