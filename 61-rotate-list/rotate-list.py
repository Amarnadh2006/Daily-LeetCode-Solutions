class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        k %= count
        if k == 0:
            return head
        temp = head
        for _ in range(count - k - 1):
            temp = temp.next
        new_head = temp.next
        temp.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        return new_head