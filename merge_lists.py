class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        r=[]
        x=list1
        y=list2
        while x:
            r.append(x.val)
            x=x.next
        while y:
            r.append(y.val)
            y=y.next
        n=ListNode()
        c=n
        for i in r:
            c.next=ListNode(i)
            c=c.next
        return n.next()
