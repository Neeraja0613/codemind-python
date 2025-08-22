class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r=[]
        while head:
            r.append(head.val)
            head=head.next
        r.sort()
        dum=ListNode()
        x=dum
        for i in r:
            x.next=ListNode(i)
            x=x.next
        return dum.next  
