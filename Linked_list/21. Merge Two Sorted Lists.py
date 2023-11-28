# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()
        res_moving_node = res_head
        curr_node1 = list1
        curr_node2 = list2

        while curr_node1 and curr_node2:
            if curr_node1.val < curr_node2.val:
                res_moving_node.next = curr_node1
                curr_node1 = curr_node1.next
            else:
                res_moving_node.next = curr_node2
                curr_node2 = curr_node2.next
            res_moving_node = res_moving_node.next
        if curr_node1:
            res_moving_node.next = curr_node1
        elif curr_node2:
            res_moving_node.next = curr_node2

        return res_head.next
