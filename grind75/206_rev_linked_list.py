# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if not head:
            return None
        stack = []
        h1 = head
        while h1:
            stack.append(h1)
            h1 = h1.next

        h = ListNode()
        new_head = h
        while stack:
            node = stack.pop()
            h.next = node
            h = node
        h.next = None

        return new_head.next

    def reverseList_2(self, head):
        curr, prev, _next = head, None, head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev


a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c
d = ListNode(4)
c.next = d
e = ListNode(5)
d.next = e

solution = Solution()
print(solution.reverseList_2(a))
