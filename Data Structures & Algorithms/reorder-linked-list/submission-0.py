# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Concept:
        We want to order [0, 1, 2, ..., n-2, n-1, n] as [0, n, 1, n-1, ...]
        Method: Fast, slow pointer
        Fast pointer will reach end, and slow pointer will be at exactly half
        We split the list in half (first half as is, and we reverse the second half.)
        Then we iterate from both heads in sync until we hit the end
        """
        slow = fast = head

        #First, we split in half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Once we split, now we reverse the second half
        second = slow.next # Jumps to right of middle, begins next chain
        prev = slow.next = None # Breaks link between lists

        # Iterate thru 2nd half until Null
        while second:
            nxt = second.next   # store the next node
            second.next = prev  # Break the forward link, make it backward
            prev = second       # Move the previous node up
            second = nxt        # Iterate down the line

        # Now we have properly reversed the list, we can start from head and prev and append accordingly
        first, second = head, prev 

        # We do just second again because
        while second:
            tmp1, tmp2 = first.next, second.next    # Store the nexts of each node
            first.next = second                     # Connect first to second
            second.next = tmp1                      # Connect second to first.next
            first, second = tmp1, tmp2              # Update/ Iterate nodes
            