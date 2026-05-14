# 328. Odd Even Linked List
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]


# Constraints:

# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def oddEvenList(head):
    odd = ListNode()
    even = ListNode()
    oddNode = odd
    evenNode = even
    isOdd = True
    while head:
        if isOdd:
            oddNode.next = head
            isOdd = False
            oddNode = oddNode.next
        else:
            evenNode.next = head
            isOdd = True
            evenNode = evenNode.next
        head = head.next
    oddNode.next = even.next
    evenNode.next = None
    return odd.next


def oddEvenListOpti(head):
    if not head or not head.next:
        return head
    odd, even = head, head.next
    evenHead = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = evenHead
    return head


LinkedList = createListNodeFromArray([1, 2, 3, 4, 5])
answer = oddEvenListOpti(LinkedList)
print("this is answer")
displayListNode(answer)
