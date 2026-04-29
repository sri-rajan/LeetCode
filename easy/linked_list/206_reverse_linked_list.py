# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


def reverseList(head):
    temp = head
    listValues = []
    while temp:
        listValues.append(temp.val)
        temp = temp.next
    finalList = head
    for i in range(len(listValues) - 1, -1, -1):
        finalList.val = listValues[i]
        finalList = finalList.next
    return


def reverseList2(head):
    node = None
    while head:
        temp = head.next
        head.next = node
        node = head
        head = temp
    return node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end="-->")
            temp = temp.next


lnkList = LinkedList()
lnkList.append(1)
lnkList.append(2)
lnkList.append(3)
lnkList.append(4)
print("initial")
lnkList.display()

answer = reverseList2(lnkList.head)
print("\nfinal")
lnkList.display()
