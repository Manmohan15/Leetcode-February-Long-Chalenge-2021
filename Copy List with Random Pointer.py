
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if(head==None):
            return None
        s=head
        while(s!=None):
            n=Node(s.val,None,None)
            n.next=s.next
            s.next=n
            s=s.next.next
        head1=head.next
        s1=head1
        s=head
        while(s!=None):
            
            if(s.random!=None):
                s.next.random=s.random.next
            else:
                s.next.random=None  
            s=s.next.next
        while(head1.next!=None and head1!=None):
            head1.next=head1.next.next
            head1=head1.next
        return s1   
