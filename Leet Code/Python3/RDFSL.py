class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        # this function takes list head as the parameter and returns the head to the new list

        current = head  # initialize a temporary pointer
        while current and current.next: # while current and the next node exists the loop will go on
            if current.val == current.next.val: # duplicate elements
                current.next = current.next.next    # simply skip forward python will handle the freeing
            else:
                current = current.next  # if no duplicates then just move forward the list
        return head


def listTraversal(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    n = int(input())
    head = ListNode(int(input()))
    temp = head
    for i in range(1, n):
        t = int(input())
        node = ListNode(t)
        temp.next = node
        temp = temp.next
    delDupli = Solution()
    ans = delDupli.deleteDuplicates(head)
    listTraversal(ans)


