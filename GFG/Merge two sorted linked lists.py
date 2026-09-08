'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, list1, list2):
        # code here
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        temp = None
        head = None
        tail = None

        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                temp = Node(list1.data)
                list1 = list1.next
            else:
                temp = Node(list2.data)
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