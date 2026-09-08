# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        temp = None
        head = None
        tail = None

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp = ListNode(list1.val)
                list1 = list1.next
            else:
                temp = ListNode(list2.val)
                list2 = list2.next
            
            if head is None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
            
        if list1 is None:
            tail.next = list2
        if list2 is None:
            tail.next = list1

        return head