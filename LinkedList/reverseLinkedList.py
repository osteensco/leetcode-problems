# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        node = head
        stack = []
        while True:
            stack.append(node.val)
            if node.next:
                node = node.next
            else:
                break

        node = None
        while stack:
            n = stack.pop()
            if node:
                node.next = ListNode(val=n)
                node = node.next
            else:
                node = ListNode(val=n)
                head = node
        return head


