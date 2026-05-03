# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []


# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def removeElements(head, val):
    while head and head.val == val:
        head = head.next
    current = head
    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return head


head = createListNodeFromArray([1, 2, 2, 1])
val = 2
print("this is initial list")
displayListNode(head)
answer = removeElements(head, val)
print("this is answer")
displayListNode(answer)
