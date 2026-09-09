class Solution:
    def sortList(self, head):
        values = []

        while head:
            values.append(head.val)
            head = head.next

        values.sort()

        dummy = ListNode(0)
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next