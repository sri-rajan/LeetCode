# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

from utils.ListNode import ListNode, createListNodeFromArray, displayListNode


def mergeKLists(lists):
    if len(lists) <= 0:
        return

    dummy = ListNode(0, lists[0])
    for i in range(1, len(lists)):
        currentLinkedList = lists[i]
        curr = currentLinkedList
        masterList = dummy
        while curr:
            while masterList and masterList.next:
                if masterList.next.val > curr.val:
                    break
                masterList = masterList.next
            currTemp = curr
            curr = curr.next
            temp = masterList.next
            masterList.next = currTemp
            masterList.next.next = temp
    return dummy.next


def mergeKListsOpti(lists):
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        temp = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            temp.append(merge_list(l1, l2))
        lists = temp
    return lists[0]


# this is the util of mergeKlistsOpti function
def merge_list(l1, l2):
    mergedList = ListNode()
    node = mergedList
    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    if l1:
        node.next = l1
    else:
        node.next = l2
    return mergedList.next


LinkedList1 = createListNodeFromArray([1, 4, 5])
LinkedList2 = createListNodeFromArray([1, 3, 4])
LinkedList3 = createListNodeFromArray([2, 6])
allLinkedList = [LinkedList1, LinkedList2, LinkedList3]
answer = mergeKListsOpti(allLinkedList)
print("this is answer")
displayListNode(answer)
