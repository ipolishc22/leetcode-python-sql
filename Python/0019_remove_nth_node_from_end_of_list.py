# 19 Remove Nth Node From End of List
#
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we create a dummy node at the beginning of the list
        dummy = ListNode(0, head)

        # add two pointers
        left = dummy
        right = head 

        # the distance between them should be n
        while n > 0 and right:
            right = right.next
            n -= 1

        # keep moving until the right one hits null
        while right:
            left = left.next
            right = right.next

        # reassign the next of the left node
        left.next = left.next.next

        # return dummy.next as it is pointint to the real head
        return dummy.next
    


