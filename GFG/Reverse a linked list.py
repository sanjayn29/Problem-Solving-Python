""" Structure of Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        temp1 = None
        temp2 = None
        while head is not None:
            temp2 = head.next
            head.next = temp1
            temp1 = head
            head = temp2
        head = temp1
        return head