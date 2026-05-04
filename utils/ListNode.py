class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createListNodeFromArray(list):
    head = ListNode(list[0])
    curr = head
    for i in range(1, len(list)):
        curr.next = ListNode(list[i])
        curr = curr.next
    return head


def displayListNode(head):
    print("this is displaying")
    temp = head
    while temp:
        print(temp.val, end="-->")
        temp = temp.next
    print("\n")
