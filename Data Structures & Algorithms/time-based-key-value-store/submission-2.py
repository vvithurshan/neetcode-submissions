from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.hash[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.hash:
            return ""

        l, r = 0, len(self.hash[key]) - 1

        res = ""

        while l <= r:
            m = l + (r - l)//2

            if self.hash[key][m][1] <= timestamp:
                res = self.hash[key][m][0]
                l = m + 1

            else:
                r = m - 1

        return res