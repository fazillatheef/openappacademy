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

def mergelist(list1,list2):    
    newNode = ListNode(0)
    fNode = newNode
    while (list1 and list2) is not None:
        if list1.val < list2.val:
            newNode.next = list1
            list1 = list1.next
        else:
            newNode.next = list2
            list2 = list2.next
        newNode = newNode.next
    if list1 is None:
        newNode.next = list2
    elif list2 is None:
        newNode.next = list1
    return (fNode.next)

l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(4)
print(l1)
print(l2)
print(mergelist(l1, l2))