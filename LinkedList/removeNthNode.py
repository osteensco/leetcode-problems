# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?







# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # putting the linked list in an array produces too many edge cases
        # so utilizing two pointers and a dummy node is a better option

        # dummy node helps us avoid needing a prev variable when shifting pointers
        dummy = ListNode(next=head)
        l = dummy
        r = head

        # create an offset of the two pointers equal to n
        while n > 0:
            r = r.next
            n -= 1
        
        # shift both pointers over until end of list
        # l will be node directly prior to node that should be removed
        while r:
            r = r.next
            l = l.next

        # remove node by pointing next to next.next
        l.next = l.next.next

        # head could be the node that needs to be removed
        # so return dummy.next as new head
        return dummy.next






