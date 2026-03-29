class TimeMap:

    def __init__(self):
        self.hashMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.hashMap:
            return ""
        values = self.hashMap.get(key)
        l=0
        r = len(values)-1
        res = ""
        while l<=r:
            pos = (l+r)//2
            mid = values[pos]
            if mid[1]<=timestamp:
                res = mid[0]
                l=pos+1
            else:
                r=pos-1
        return res
