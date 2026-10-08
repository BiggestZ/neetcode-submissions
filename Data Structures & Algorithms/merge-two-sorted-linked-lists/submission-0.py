# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Concept: We want to start at the beginning of each list and iterate as follow:
        - if list1[i] < list2[i]: we append list1[i] and iterate down list 1
        - else (opposite): do the same but for list 2 
        - We will iterate for as long as both list have elements.
        - If one list is longer than the other, we need to append the rest of that list to the end of the list
        """
        # List that will hold the combined list
        # We use 2 names for 1 variable so we iterate with one while the other stays at the head
        result = node = ListNode()

        # While both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1 #  We add list1 bc that is the node object, not the whole list
                list1 = list1.next  #  Iterate down list 1
            else:
                result.next = list2
                list2 = list2.next
            # We move down to appended node for next iteration
            result = result.next 
        
        # we need to make sure that we append whatever is left over from either list incase length varied
        if list1:
            result.next = list1
        else:
            result.next = list2
        
        # At the end, we return node.next, as it point to the first element we added
        return node.next