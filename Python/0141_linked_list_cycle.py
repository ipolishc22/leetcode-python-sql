# 141 Linked List Cycle 
#
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True 
        
        return False