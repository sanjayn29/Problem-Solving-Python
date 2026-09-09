# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #edge case
        if head is None or head.next is None:
            return

        #middle
        mid = head
        temp = head
        while temp is not None and temp.next is not None:
            mid = mid.next
            temp = temp.next.next

        #reverse
        temp = mid.next
        mid.next = None
        temp2 = None
        temp3 = None
        while temp is not None:
            temp2 = temp.next
            temp.next = temp3
            temp3 = temp
            temp = temp2
        
        #merge
        first = head
        second = temp3
        while second is not None:
            n1 = first.next
            n2 = second.next
            first.next = second
            second.next = n1
            first = n1
            second = n2
        