# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False 

        slow = fast = head

        fast = fast.next

        while fast:

            if fast == slow:
                return True

            slow = slow.next
            if fast:
                fast = fast.next
                if fast:
                     fast = fast.next

            
        return False


            
        