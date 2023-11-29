# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _greatest_common_divisor(num1,num2):
            if num1 > num2:
                divisor = num2
                while divisor >0:
                    if num1 % divisor ==0 and num2 % divisor ==0 :
                        return divisor
                    divisor-=1
            else:
                divisor = num1
                while divisor >0:
                    if num1 % divisor ==0 and num2 % divisor ==0 :
                        return divisor
                    divisor-=1

        if not head:
            return None
        if not head.next:
            return head
        node1 = head
        node2 = head.next
        while node2:
            gcd = _greatest_common_divisor(node1.val,node2.val)
            new_node = ListNode(gcd)
            # connect to new node
            node1.next = new_node
            new_node.next = node2
            #move pointers
            node1 = node2
            node2 = node2.next
        return head
