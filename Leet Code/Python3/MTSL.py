# Definition of Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # In case if any one of the lists is empty then we return the other one
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # To initialize the head of the new list
        if list1.val <= list2.val:
            tail = head = ListNode(list1.val)
            list1 = list1.next
        else:
            tail = head = ListNode(list2.val)
            list2 = list2.next

        # we compare the corresponding elements of the two lists one by one and copy the smallest one to the new list till any one of the lists reaches it's end
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next

            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
                
            tail = tail.next
        
        # if anyone of the lists doesn't complete at the end then we copy the rest of the list as it is
        """while list1 is not None:
            tail.next = ListNode(list1.val)
            list1 = list1.next
            tail = tail.next
        
        while list2 is not None:
            tail.next = ListNode(list2.val)
            list2 = list2.next
            tail = tail.next"""

        # instead of copying the remaining elements we just link the tail of the new list with the current node of the lists
        if list1 is not None:
            tail.next = list1
            
        
        if list2 is not None:
            tail.next = list2

        return head


if __name__ == "__main__":

    # One possible improvement can be to handle if no input is given
    n = int(input("Enter the first list size: "))
    t = int(input())
    tail1 = head1 = ListNode(t)
    for _ in range(n-1):
        t = int(input())
        tail1.next = ListNode(t)
        tail1 = tail1.next

    n1 = int(input("Enter the second list size: "))
    t = int(input())
    tail2 = head2 = ListNode(t)
    for _ in range(n1 - 1):
        t = int(input())
        tail2.next = ListNode(t)
        tail2 = tail2.next
    
    sol = Solution()
    ans = sol.mergeTwoLists(head1, head2)

    while ans is not None:
        print(ans.val)
        ans = ans.next

    