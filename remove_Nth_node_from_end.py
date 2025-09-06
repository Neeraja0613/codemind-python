class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r=[]
        x=head
        while x:
            r.append(x.val)
            x=x.next
        r.pop(len(r)-n)
        b=ListNode()
        c=b
        for i in r:
            c.next=ListNode(i)
            c=c.next
        return b.next
