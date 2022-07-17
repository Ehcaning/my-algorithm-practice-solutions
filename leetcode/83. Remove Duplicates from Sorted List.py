class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head

        while ptr:
            while ptr.next and ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            ptr = ptr.next

        return head
