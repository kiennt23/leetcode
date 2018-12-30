# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '[' + self.val + ']'


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first_tortoise = head
        hare = head
        first_iteration = True
        while first_iteration or first_tortoise != hare:
            if hare.next is None or hare.next.next is None:
                # There is no circle
                return None
            hare = hare.next.next
            first_tortoise = first_tortoise.next
            first_iteration = False

        second_tortoise = head
        while first_tortoise != second_tortoise:
            first_tortoise = first_tortoise.next
            second_tortoise = second_tortoise.next

        return first_tortoise
