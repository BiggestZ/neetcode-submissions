# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We need to traverse the list, and swap its pointers for each node
        if not head:
            return None

        # Concept:
        # We want to store the next node, then break that link, and switch
        # null -> a -> b -> c
        # We store b and break that link. we store curr as prev
        # null -> a | b
        curr = head
        prev = None
        while curr:
            # Store in advance
            nxt = curr.next
            
            # Now we perform the swap
            curr.next = prev # null <- a
            # update prev
            prev = curr
            # Move down the line
            curr = nxt
        
        # We return prev bc curr will end at null
        return prev
    