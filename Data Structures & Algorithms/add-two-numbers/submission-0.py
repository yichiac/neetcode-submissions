# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry!=0:
            if l1:
                l1val = l1.val
            else:
                l1val = 0
            if l2:
                l2val = l2.val
            else:
                l2val = 0
            
            s = l1val + l2val + carry
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        return dummy.next