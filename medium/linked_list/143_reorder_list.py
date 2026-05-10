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
from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def reorderList(head):
    curr = head
    while curr and curr.next and curr.next.next:
        nextTemp = curr.next
        lastTemp = None
        tail = None
        dummy = curr
        while dummy.next:
            lastTemp = dummy
            dummy = dummy.next
        tail = dummy
        curr.next = tail
        lastTemp.next = None
        curr.next.next = nextTemp
        curr = curr.next.next
    return head


def reorderListOpti(head):
    # split the list into two and reverse the second half
    slow = fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    # reverse the second path
    node = None
    while second:
        temp = second.next
        second.next = node
        node = second
        second = temp

    first = head
    second = node
    # merge both first and second list
    while second:
        firstTemp = first.next
        secondTemp = second.next
        first.next = second
        second.next = firstTemp
        first = firstTemp
        second = secondTemp
    return head


LinkedList = createListNodeFromArray([1, 2, 3, 4, 5])
answer = reorderListOpti(LinkedList)
print("this is answer")
displayListNode(answer)
