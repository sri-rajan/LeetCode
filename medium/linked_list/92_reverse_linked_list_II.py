# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]


# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def reverseBetween(head, left, right):
    if not head or left == right:
        return head
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    tail = prev.next
    for _ in range(right - left):
        tmp = prev.next
        prev.next = tail.next
        tail.next = tail.next.next
        prev.next.next = tmp

    return dummy.next


LinkedList = createListNodeFromArray([1, 2, 3, 4, 5])
answer = reverseBetween(LinkedList, 2, 4)
print("this is answer")
displayListNode(answer)
