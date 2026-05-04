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

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def removeNthFromEnd(head, n):
    res = ListNode(0, head)
    removeItem = res
    for i in range(n):
        head = head.next
    while head:
        head = head.next
        removeItem = removeItem.next
    removeItem.next = removeItem.next.next
    return res.next


linkedList = createListNodeFromArray([1, 2, 3, 4, 5])
answer = removeNthFromEnd(linkedList, 2)

displayListNode(answer)
