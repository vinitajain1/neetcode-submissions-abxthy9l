# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val<other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap,NodeWrapper(lst))
        
        while minHeap:
            nodeWrapper = heapq.heappop(minHeap)
            curr.next = nodeWrapper.node
            curr = curr.next
            if nodeWrapper.node.next:
                heapq.heappush(minHeap,NodeWrapper(nodeWrapper.node.next))
        return dummy.next
        