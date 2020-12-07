# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

class Solution0:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        p=l2
        if l1.val<=l2.val:
            p=l1
            l1=l1.next
        else:
            l2=l2.next
        p.next=self.mergeTwoLists(l1,l2)
        return p

class Solution0:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre=dummy = ListNode(-1)
        while l1 and l2:
            if l1.val<=l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2=l2.next
            pre=pre.next
        if l1:pre.next=l1
        else:pre.next=l2
        return dummy.next
        


class Solution0:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=p=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        if l1:
            dummy.next=l1
        elif l2:
            dummy.next=l2

        return p.next
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
