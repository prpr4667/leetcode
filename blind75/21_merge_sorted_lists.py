You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode(-1)
        end = head

        while list1 and list2:
            if list1.val < list2.val:
                end.next = list1
                list1 = list1.next
            else:
                end.next = list2
                list2 = list2.next
            end = end.next
        if list1:
            end.next = list1
        elif list2:
            end.next = list2

        return head.next