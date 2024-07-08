# 143. Reorder List
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # using a stack to reverse order list
        stack = []
        node = head
        
        # populate stack
        while node:
            stack.append(node)
            node = node.next
        node = head

        # we only need the last half of the list, so 
        # grap top half of stack.
        # this will give us all nodes we need to reposition
        stack = stack[len(stack)//2:]
        # isolate nodes to avoid listnode cycle (infinite pointer loop)
        for i in stack:
            i.next = None
        
        while stack:
            # set a pointer to allow list to be split
            # grab top of stack and set it next in list
            # move our pointer to the next node
            n = node.next
            node.next = stack.pop()
            node = node.next 

            # when we still have nodes in our stack we 
            # set the next node to the original next that we 
            # pointed to with n, and then move to that node
            if stack:
                node.next = n
                node = node.next
            # if we're through our stack n will point to our current node if n is
            # odd, where n = len(LinkedList), so to avoid
            # an infinite linked list that points to itself, we just set next to None instead of n
            else:
                node.next = None







