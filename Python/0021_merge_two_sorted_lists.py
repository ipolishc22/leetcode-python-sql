# 21 Merge Two Sorted Lists
# 
# Time complexity: O(n+m)
# Space complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next


        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next