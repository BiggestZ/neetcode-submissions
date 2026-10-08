# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Concept:
        We use fast/slow pointers. s += 1, f += 2.
        We iterate while f not null. If f and s ever equal, return false
        we return true outside the loop
        """
        slow = head
        fast = head
        
        # While fast is not null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            # If they are equal, True
            if slow == fast:
                return True

        return False
        