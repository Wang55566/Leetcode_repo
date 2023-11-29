# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        new_set = set()
        current_A = headA
        current_B = headB
        while current_A:
            new_set.add(current_A)
            current_A = current_A.next
        while current_B:
            if current_B in new_set:
                return current_B
            new_set.add(current_B)
            current_B = current_B.next
        return None
