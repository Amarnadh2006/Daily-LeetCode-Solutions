# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        odd = head
        even = head.next
        last = even
        while odd.next != None and even.next != None:
            odd.next = odd.next.next
            odd = odd.next
            if even.next.next != None:
                even.next = even.next.next
                even = even.next
            else:
                even.next = None
                break
        odd.next = last
        return head
        
        

        