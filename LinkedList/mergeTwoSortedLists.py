# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.






# Definition for singly-linked list.
# solution if linked list is ordered
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # handle edge case where nothing is passed in
        if not list1 and not list2:
            return

        node = ListNode()
        output = node

        while True:

            if not list1:
                # we can just use the rest of the remaining linked list if nothing left in the other
                node.val = list2.val
                node.next = list2.next
                break
            elif not list2:
                node.val = list1.val
                node.next = list1.next
                break
            
            elif list1.val <= list2.val:
                node.val = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                node.val = list2.val
                list2 = list2.next

            if not output:
                output = node

            if list1 or list2:
                node.next = ListNode()
                node = node.next
            else:
                break

        return output









# Solution for O(1) memory

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        firsth, lasth = node, node.next
        
        while lasth and lasth.next:
            firsth = firsth.next
            lasth = lasth.next.next
        
        second = firsth.next
        # break off last node in first half of list
        firsth.next = None
        prev = None
        
        while second:
            # set the pointer to shift to at end of iteration
            n = second.next
            # reverse the next pointer to the previous node
            second.next = prev
            # shift prev to current node
            prev = second
            # shift current node to original next pointer
            second = n
            

        node = head
        node2 = prev

        while node2:
            # set pointers to shift at end of iteration
            n1 = node.next
            n2 = node2.next
            #             [n1]
            # node(1) -> node1(2) -> node1(3) -> ...
            #              [n2]
            # node2(1) -> node2(2) -> node2(3) -> ...

            #                         [n2]
            # node(1) -> node2(1) -> node2(2) -> node2(3) -> ...
            node.next = node2
            #                         [n1]
            # node(1) -> node2(1) -> node1(2) -> node1(3) -> ...
            node2.next = n1
            # shift pointers
            node = n1
            #                                     [n1]
            # node(1) -> node2(1) -> node1(2) -> node1(3) -> ...
            node2 = n2
            #              [n2]
            # node2(2) -> node2(3) -> ...

        return head

