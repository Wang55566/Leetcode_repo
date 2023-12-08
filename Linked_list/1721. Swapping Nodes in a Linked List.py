# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        index = 0
        curr_node = head
        #find j index
        while curr_node:
            index +=1
            curr_node = curr_node.next
        j = index - k + 1

        #get the 4 pointers
        index = 0
        curr_node = head
        pre_k, p1, pre_j, p2 = None, None, None, None
        while curr_node:
          index +=1

          if index == k-1:
            pre_k = curr_node
          if index == k:
            p1 = curr_node
          if index == j-1:
            pre_j = curr_node
          if index == j:
            p2 = curr_node
          curr_node = curr_node.next

        #swapping
        if pre_k :
          pre_k.next = p2
        else:
          head = p2
        if pre_j:
          pre_j.next = p1
        else:
          head = p1

        last_node = p2.next
        p2.next = p1.next
        p1.next = last_node
        return head
