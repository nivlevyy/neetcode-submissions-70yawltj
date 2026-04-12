# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2: 
            return list1
        
       
        p_l1=list1
        p_l2=list2
        start=temp=ListNode()
        while temp is not None:
            
            if not p_l1 or not p_l2:
                break
            if p_l1.val > p_l2.val:
                temp.next =p_l2
                p_l2=p_l2.next
            else:
                temp.next =p_l1
                p_l1=p_l1.next
            temp=temp.next
        if not p_l1:
            temp.next=p_l2
        if not p_l2:
            temp.next=p_l1

        return start.next


                


        
