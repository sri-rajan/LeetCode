# 86. Partition List
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.


# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]


# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def partition(head, x):
    dummy = ListNode(0, head)
    left = dummy
    right = dummy

    while right and right.next:
        if right.next.val < x:
            if left == right:
                left = left.next
                right = right.next
            else:
                temp = right.next
                right.next = temp.next

                temp.next = left.next
                left.next = temp
                left = left.next
        else:
            right = right.next
    return dummy.next


def partitionOpti(head, x):
    sList = ListNode()
    bList = ListNode()
    small = sList
    big = bList

    while head:
        if head.val < x:
            small.next = head
            small = small.next
        else:
            big.next = head
            big = big.next
        head = head.next
    small.next = bList.next
    big.next = None
    return sList.next


LinkedList = createListNodeFromArray([1, 4, 3, 0, 2, 5, 2])

answer = partitionOpti(LinkedList, 3)
print("this is answer")
displayListNode(answer)
