class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map.get(key)
        l=0
        r=len(values)-1
        res = ""
        while l<=r:
            pos = (l+r)//2
            midVal = values[pos]
            if midVal[1]<=timestamp:
                res=midVal[0]
                l=pos+1
            else:
                r=pos-1
        return res

