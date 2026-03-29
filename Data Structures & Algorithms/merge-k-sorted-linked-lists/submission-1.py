# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self,other):
        return self.val<other.val

# class NodeWrapper:
#     def __init__(self,node):
#         self.node = node
#     def __lt__(self,other):
#         return self.node.val<other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap,lst)
        
        while minHeap:
            node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minHeap,node.next)
        return dummy.next
        