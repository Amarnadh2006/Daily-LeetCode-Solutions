# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        nn = head.next
        while(curr.next != None):
            curr.next = prev
            prev= curr
            curr = nn
            nn=nn.next 
        curr.next = prev
        head = curr 
        curr = curr.next
        head.next = None
        while (curr != None):
            if curr.val >= head.val:
                prev = curr
                curr = curr.next
                prev.next = head
                head = prev 
            else:
                curr = curr.next
        return head



        