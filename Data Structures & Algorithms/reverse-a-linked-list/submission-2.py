# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurse(self, li):
        if li != None:
            if li.next != None:
                if li.next.next == None:
                    li.next.next = li
                    x = li.next
                    li.next = None
                    return x
                else:
                    new_head = self.recurse(li.next)
                    li.next.next = li
                    li.next = None
                    return new_head
            else:
                return li
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = self.recurse(head)
        return new_head