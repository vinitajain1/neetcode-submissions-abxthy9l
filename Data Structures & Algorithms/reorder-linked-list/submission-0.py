# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque()
        node = head.next
        while node:
            queue.append(node)
            node = node.next
        node = head
        front = False
        while queue:
            elem = None
            if front:
                elem = queue.popleft()
            else:
                elem = queue.pop()
            front = not front
            node.next = elem
            node = elem        
        node.next = None

