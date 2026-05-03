# 83. Remove Duplicates from Sorted List
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


# Constraints:


# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    current = head
    count = 0
    while current and current.next:
        count += 1
        if count > 20:
            break
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


head = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)

head.next = node2
node2.next = node3

answer = deleteDuplicates(head)
while answer:
    print(answer.val, end="-->")
    answer = answer.next
