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
        # top of stack needs to be less than current node
        # this will let us find all nodes we need to reposition
        while node.val < stack[-1].val: 
            # only caveat is when n is even where n = len(LinkedList)
            # on the last iteration the next node (which is the top of our stack) will equal the current node
            # current node will already have this next node so we skip this iteration, otherwise node.next will be set to None erroneously
            if node.next.val == stack[-1].val:
                break

            # main algo

            # set a temp variable, n
            n = node.next
            # set next to node in top of stack
            node.next = stack.pop()
            # move pointer to the next node
            node = node.next 
            
            # cleanup next pointer on node in top of stack to avoid listnode cycle (infinite pointer loop)
            stack[-1].next = None
            # set next to original next, results in us essentially inserting the node between node and node.next
            # 1 -> 2 -> 3 results in 1 -> 3 -> 2
            node.next = n
            # move our pointer again if we aren't at end of list (only applies when n is odd, where n = len(LinkedList)
            if node.next:
                node = node.next


