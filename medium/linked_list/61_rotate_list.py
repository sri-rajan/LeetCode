# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.


# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def rotateRight(head, k):
    # getting node count
    if not head or not head.next or k == 0:
        return head
    nodeCount = 1
    tail = head
    while tail and tail.next:
        tail = tail.next
        nodeCount += 1
    rotateCount = k % nodeCount
    if rotateCount == 0:
        return head

    changePoint = head
    for i in range(nodeCount - rotateCount - 1):
        changePoint = changePoint.next
    rotateNode = changePoint.next
    changePoint.next = None
    tail.next = head

    return rotateNode


LinkedList = createListNodeFromArray([1, 2, 3, 4, 5])
answer = rotateRight(LinkedList, 2)
print("this is answer")
displayListNode(answer)
