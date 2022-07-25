#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order, and each of their nodes contains a single digit. 
#Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        l = self.next
        result = str(self.val)
        while l != None:
            result += str(l.val)
            l = l.next
        return result

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ResultNode = None
    TempNode = None
    carry = 0
    while l1 != None or l2 != None:
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        sum = l1.val + l2.val + carry
        carry = 0
        if sum > 9:
            carry = 1
            sum = sum % 10
        if TempNode == None:
            ResultNode = ListNode(sum)
            TempNode = ResultNode
        else:
            TempNode.next = ListNode(sum)
            TempNode = TempNode.next
        l1 = l1.next
        l2 = l2.next
    if carry == 1:
        TempNode.next = ListNode(carry)
    return ResultNode
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
print(l1)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(l2)
print(addTwoNumbers(l1, l2))