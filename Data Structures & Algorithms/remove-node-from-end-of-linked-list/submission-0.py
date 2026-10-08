# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Concept:
        We want to remove the Nth element from the end.
        Solution: 2 pointers. We set a to the head, and move b N steps from the head. 
        We then iterate until b is null, in which case a will point to the value we need to remove
        *Note: We actually want a to stop at n-1, so we can perform a node skip
        To do that, we create a dummy node that points to head and start a from there 
        """

        if not head:
            return []

        # Initialized the dummy node
        dummy = ListNode(-1, head)

        # Init. 2 pointers
        a, b = dummy, head

        # Iterate b N times over
        for i in range(n):
            b = b.next


        # Iterate until b is null
        while b:
            a = a.next
            b = b.next

        # Now we modify a to skip n
        a.next = a.next.next

        # Lastly we return the head
        return dummy.next