class TreeNode:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
class MyCalendar:
    
    def __init__(self):
        self.root = None

    def _insert(self,start,end,node):
        if end<=node.start:
            if not node.left:
                node.left = TreeNode(start,end)
                return True
            return self._insert(start,end,node.left)
        elif start>=node.end:
            if not node.right:
                node.right = TreeNode(start,end)
                return True
            return self._insert(start,end,node.right)
        else:
            return False
        
    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime,endTime)
            return True
        return self._insert(startTime,endTime,self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)