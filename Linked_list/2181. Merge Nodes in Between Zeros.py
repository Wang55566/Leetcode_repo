# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        curr_node = head.next
        res_list = ListNode()
        curr_res_node = res_list
        while curr_node:
            if curr_node.val != 0:
                sum += curr_node.val
            else:
                curr_res_node.next = ListNode(sum)
                curr_res_node = curr_res_node.next
                sum = 0
            curr_node = curr_node.next
        return res_list.next
