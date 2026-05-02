# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


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
        print("\n")


def mergeTwoLists(list1, list2):
    dummy = LinkedList()
    curr = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
    return dummy.next


lnkList1 = LinkedList()
lnkList1.append(1)
lnkList1.append(2)
lnkList1.append(4)

lnkList2 = LinkedList()
lnkList2.append(1)
lnkList2.append(3)
lnkList2.append(4)

print("initial one")
lnkList1.display()
print("initial two")
lnkList2.display()

answer = mergeTwoLists(lnkList1.head, lnkList2.head)
print("final")
count = 0
while answer:
    count += 1
    if count > 10:
        break
    print(answer.val)
    answer = answer.next
