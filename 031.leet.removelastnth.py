# Remove nth node from the last of the linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        l = self.next
        result = str(self.val)
        while l != None:
            result += ',' + str(l.val)
            l = l.next
        return result
# Clever bit is first moving a pointer n positions, then keep a pointer at the head
# After that move both together through the linked list until the first pointer reaches the end.
# When that happens use the second pointer to make the changes
# +2 becomes -2 because the second pointer is alway 2 positions behind the first one
def removeNthFromEnd( head, n):
    frontN, backN = head, head

    # move front pointer n times
    for _ in range(n):
        if frontN.next:
            frontN = frontN.next
        else:
            head = head.next
            return head
    
    while frontN.next:
        # move front and back pointer together
        # until front reach the end of LinkedList
        frontN = frontN.next
        backN = backN.next
    
    backN.next = backN.next.next
    
    return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
print(l1)

print(removeNthFromEnd(l1, 2))