# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r=[]
        while head:
            r.append(head.val)
            head=head.next
        x=r[::-1]
        dum=ListNode()
        a=dum
        for i in x:
            a.next=ListNode(i)
            a=a.next
        return dum.next
