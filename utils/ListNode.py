import random


class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def createListNodeFromArray(list):
    head = ListNode(list[0])
    curr = head
    for i in range(1, len(list)):
        curr.next = ListNode(list[i])
        curr = curr.next
    return head


def createListNodeWithRandom(list):
    head = ListNode(list[0])
    hash = {0: head}
    curr = head
    for i in range(1, len(list)):
        curr.next = ListNode(list[i])
        curr = curr.next
        hash[i] = curr
    curr = head
    while curr:
        randomIndex = random.randint(0, len(list) - 1)
        curr.random = hash[randomIndex]
        curr = curr.next
    return head


def displayListNodeWithRandom(head):
    temp = head
    while temp:
        randomVal = temp.random.val if temp.random else None
        print(f"({temp.val}, {randomVal})", end=" --> ")
        temp = temp.next
    temp = head
    print("\n", end="")
    while temp:
        randomVal = temp.random
        print(f"({hex(id(temp))[-4:]}, {hex(id(randomVal))[-4:]})", end=" --> ")
        temp = temp.next

    print("\n", end="")


def displayListNode(head):
    temp = head
    while temp:
        print(temp.val, end="-->")
        temp = temp.next
    print("\n", end="")
