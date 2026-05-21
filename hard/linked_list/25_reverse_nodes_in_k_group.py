# 25. Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]


# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000


# Follow-up: Can you solve the problem in O(1) extra memory space?

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def reverseKGroup(head, k):
    if not head or k <= 1:
        return head
    listLength = 0
    temp = head
    while temp:
        temp = temp.next
        listLength += 1
    reverseCount = listLength // k
    dummy = ListNode(0, head)
    previoustail = dummy
    curr = head
    for i in range(reverseCount):
        node = None
        tail = curr
        for i in range(k):
            temp = curr.next
            curr.next = node
            node = curr
            curr = temp
        previoustail.next = node
        tail.next = curr
        previoustail = tail

    return dummy.next


LinkedList = createListNodeFromArray([1, 2, 3, 4, 5])
answer = reverseKGroup(LinkedList, 2)
print("this is answer")
displayListNode(answer)
