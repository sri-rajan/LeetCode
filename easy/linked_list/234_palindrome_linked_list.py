# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false


# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9


# Follow up: Could you do it in O(n) time and O(1) space?

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def isPalindrome(head):
    list = []
    while head:
        list.append(head.val)
        head = head.next

    return list == list[::-1]


def isPalindromeWithTwoPointer(head):
    list = []
    while head:
        list.append(head.val)
        head = head.next
    l = 0
    r = len(list) - 1
    while l < r:
        if list[l] != list[r]:
            return False
        l += 1
        r -= 1
    return True


def isPalindromWithSlowfast(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    node = None
    while slow:
        temp = slow.next
        slow.next = node
        node = slow
        slow = temp

    first, second = head, node
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True


def isPalindromWithStack(head):
    slow = head
    fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        fast = fast.next.next
        slow = slow.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True


head = createListNodeFromArray([1, 2, 2, 1])
displayListNode(head)
answer = isPalindromWithStack(head)
print("this is answer", answer)
