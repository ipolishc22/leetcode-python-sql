# 206 Reverse Linked List
# 
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    # recursive solution better for space complexity 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead



    # iterative solution
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseListIter(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
