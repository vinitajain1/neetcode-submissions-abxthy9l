class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] = self.freq[val]+1
        self.maxFreq = max(self.maxFreq,self.freq[val])
        self.group[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val]-=1
        if not self.group[self.maxFreq]:
            self.maxFreq-=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()