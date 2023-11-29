# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        # solution2
        curr = head
        nxt = head.next

        while nxt:
            if curr.val == nxt.val:
                curr.next = nxt.next
                nxt = nxt.next
            else:
                curr = nxt
                nxt = nxt.next
        return head






        # # solution1
        # dummy = ListNode()
        # curr_d = dummy
        # if not head:
        #     return None
        # dummy.next = ListNode(head.val)
        # curr_d = curr_d.next
        # if not head.next:
        #     return head
        # curr_h = head.next

        # while curr_h:
        #     print(curr_h.val, curr_d.val)
        #     if curr_h.val != curr_d.val:
        #         curr_d.next = ListNode(curr_h.val)
        #         curr_d = curr_d.next
        #     curr_h = curr_h.next
        # return dummy.next
